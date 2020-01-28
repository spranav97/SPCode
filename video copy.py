from Positioning2 import detect
import cv2

ctr = 1
cam = cv2.VideoCapture(0)
result = False
while 1:
    ret, img = cam.read()
    if ret:
        #print(result)
        if ctr == 30:
            result = detect(img, False)
            ctr = 1
        else:result = detect(img, result)
        #cv2.imshow('Video', img)
        if cv2.waitKey(1) & 0xFF == ord('q') :break
        ctr += 1

cam.release()
cv2.destroyAllWindows()
