import cv2
from math import pi,acos,asin,atan,degrees

def shape(c):
    shape = False
    approx = cv2.approxPolyDP(c, 0.04 * cv2.arcLength(c, True), True)
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
    print(shape)
    return [shape,(cx,cy),distance]

def orientation(i):
    j = i.copy()
    g = cv2.cvtColor(i, cv2.COLOR_BGR2GRAY)
    r, t = cv2.threshold(g, 127, 255, cv2.THRESH_BINARY)
    cnts, h = cv2.findContours(
        t.copy(),
        cv2.RETR_TREE,
        cv2.CHAIN_APPROX_SIMPLE,
    )
    #print(h)
    try:
        maxi, ind = 0, 0
        for n, i in enumerate(h[0]):
            if maxi < i[3]:
                maxi = i[3]
                if i[0] == -1 and i[1] == -1 and i[2] == -1: ind = n
        if ind and maxi:
            inside = shape(cnts[h[0][h[0][ind][-1]][-1]])
            out = shape(cnts[h[0][ind][-1]])
            if inside[0] and out[0]:
                cv2.ellipse(
                    j,
                    inside[1],
                    (100,50),
                    0,
                    0,
                    360,
                    (0,0,255),
                    1
                )
                cv2.arrowedLine(j, inside[1], out[1],(0, 0, 255), 1)
                cv2.circle(j,out[1],20,(255,0,0),2)
            #cv2.waitKey(0)
    except:
        pass
    cv2.imshow('code', j)
    cv2.imshow('gray', t)

'''i=cv2.imread('pic2.png')
detect_code(i)'''