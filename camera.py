import cv2

capture = cv2.VideoCapture(0)

'''
3가로 4세로 값 설정
capture(3, 720)
capture(4, 1080)

'''

while True:
    ret, frame = capture.read()

    cv2.imshow('test camera', frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cv2.destroyAllWindows()