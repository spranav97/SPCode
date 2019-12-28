import cv2
import numpy as np
import math
i=cv2.imread('D:\Vault\Protonium\VIT Delivery\SPCode\codes\pic1.png')
g=cv2.cvtColor(i.copy(),cv2.COLOR_BGR2GRAY)
r,b=cv2.threshold(g,100,255,cv2.THRESH_BINARY)


def shape(c):
    shape = False
    approx = cv2.approxPolyDP(c, 0.05 * cv2.arcLength(c, True), True)
    if len(approx) == 4:
        rect = cv2.minAreaRect(approx)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        #print(box)
        cx=(box[0][0]+box[2][0])//2
        cy=(box[0][1]+box[2][1])//2
        distance = [
            math.sqrt(sum([(a - b) ** 2 for a, b in zip(box[0], box[1])])),
            math.sqrt(sum([(a - b) ** 2 for a, b in zip(box[1], box[2])])),
            math.sqrt(sum([(a - b) ** 2 for a, b in zip(box[2], box[3])])),
            math.sqrt(sum([(a - b) ** 2 for a, b in zip(box[3], box[0])]))
        ]
        '''
        print(distance)
        cv2.drawContours(i,[box],-1,(0,0,225),1)
        cv2.circle(i,(cx,cy),20,(255,0,0),1)
        '''
        '''
        ar = w / float(h)
        shape = True if ar >= 0.95 and ar <= 1.05 else False
        '''
        shape = True
    return [shape,(cx,cy),distance]


cnts,h=cv2.findContours(b,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
for cnt in cnts:
    shape(cnt)
#cv2.drawContours(i,cnts,-1,(0,0,225),2)

cv2.imshow('image',i)
cv2.waitKey(0)