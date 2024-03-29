import os
import cv2
import numpy as np
import tensorflow as tf
import sys

sys.path.append("..") #object detection폴더 안에 있어야함

from utils import label_map_util
from utils import visualization_utils as vis_util
''' 폴더 밖에 있는경우
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as vis_util
'''
MODEL_NAME = 'inference_graph' #사용할 그래프
VIDEO_NAME = '지상낮720.mp4' #사용할 영상 웹캠 구동시 주석

CWD_PATH = os.getcwd() #현재 작업중인 폴더

PATH_TO_CKPT = os.path.join(CWD_PATH,MODEL_NAME,'frozen_inference_graph.pb')
PATH_TO_LABELS = os.path.join(CWD_PATH,'training','labelmap.pbtxt')
PATH_TO_VIDEO = os.path.join(CWD_PATH, VIDEO_NAME) #그래프 라벨 영상 경로 설정 웹캠 구동시 주석
NUM_CLASSES = 2 #라벨맵에 있는 데이터 분류 량

label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
category_index = label_map_util.create_category_index(categories)

detection_graph = tf.Graph() #텐서그래프 메모리 적재
with detection_graph.as_default():
    od_graph_def = tf.GraphDef()
    with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
        serialized_graph = fid.read()
        od_graph_def.ParseFromString(serialized_graph)
        tf.import_graph_def(od_graph_def, name='')
'''
own dataset을 가졌을때 gpu성능을 가져야하는 기이한 현상 해결불가...
'''
    sess = tf.Session(graph=detection_graph)

image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')#이미지 텐서
detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')#감지 박스

detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')#물체 인식률
detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')#감지 클래스 라벨

num_detections = detection_graph.get_tensor_by_name('num_detections:0')#이미지값

video = cv2.VideoCapture(PATH_TO_VIDEO)
'''
웹캠으로 구동시 video = cv2.VideoCapture(0)
'''
while(video.isOpened()):
    ret, frame = video.read()
    frame_expanded = np.expand_dims(frame, axis=0)

    (boxes, scores, classes, num) = sess.run(#프레임 단위로 이미지 값에 텐서그래프 정보를 씌움
        [detection_boxes, detection_scores, detection_classes, num_detections],
        feed_dict={image_tensor: frame_expanded})

    vis_util.visualize_boxes_and_labels_on_image_array(#결과값 생성
        frame,
        np.squeeze(boxes),
        np.squeeze(classes).astype(np.int32),
        np.squeeze(scores),
        category_index,
        use_normalized_coordinates=True,
        line_thickness=8,
        min_score_thresh=0.60)

    cv2.imshow('Object detector', frame)

    if cv2.waitKey(1) == ord('q'):
        break

video.release()
cv2.destroyAllWindows()

