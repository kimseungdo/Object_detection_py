import os
import cv2
import numpy as np
import tensorflow as tf
import sys

sys.path.append("..")

from utils import label_map_util
from utils import visualization_utils as vis_util

MODEL_NAME = 'inference_graph'
VIDEO_NAME = '지상낮720.mp4'
