#from detect import detect_code
from orientation import orientation

import cv2

cam = cv2.VideoCapture(0)
while 1:
    ret, img = cam.read()
    #if ret == 1: detect_code(img)
    if ret == 1: orientation(img)
    if cv2.waitKey(1) == 27: break

cam.release()
cv2.destroyAllWindows()