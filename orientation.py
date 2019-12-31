import cv2


def shape(c):
    shape = False
    approx = cv2.approxPolyDP(c, 0.03 * cv2.arcLength(c, True), True)
    cx,cy=0,0
    if len(approx) == 4:
        rect = cv2.minAreaRect(approx)
        box = cv2.boxPoints(rect)
        #print(box)
        cx = int(box[0][0] + box[2][0]) // 2
        cy = int(box[0][1] + box[2][1]) // 2
        shape = True
    #print(shape)
    #print(cx,cy)
    return [shape, (cx, cy)]

def orientation(i):
    j = i.copy()
    g = cv2.cvtColor(i, cv2.COLOR_BGR2GRAY)
    r, t = cv2.threshold(g, 100, 255, cv2.THRESH_BINARY)
    cnts, h = cv2.findContours(t.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE,)
    #print(h)
    ind = []
    if type(h)!=type(None):
        for n, i in enumerate(h[0]):
                if i[0] == i[1] == i[2] == -1:
                    ind.append(n)
        for m in ind:
            out = shape(cnts[h[0][h[0][m][-1]][-1]])
            inside = shape(cnts[h[0][m][-1]])
            this = shape(cnts[h[0][m][-2]-1])
            if inside[0] and out[0]:
                '''
                print('out',h[0][m][-1],'in',h[0][h[0][m][-1]][-1])
                print(inside[1], out[1])
                '''
                #print(h)
                cv2.arrowedLine(j, out[1], inside[1], (0, 0, 255), 1)
                cv2.circle(j, inside[1], 20, (255, 0, 0), 2)
                cv2.drawContours(j,cnts[h[0][h[0][m][-1]][-1]],-1,(0,0,255),2)
                cv2.drawContours(j,cnts[h[0][m][-1]],-1,(255,0,0),2)
            # cv2.waitKey(0)
    cv2.imshow("code", j)
    cv2.imshow("gray", t)


"""i=cv2.imread('pic2.png')
detect_code(i)"""

