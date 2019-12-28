import cv2


def shape(c):
    shape = 'h'
    approx = cv2.approxPolyDP(c, 0.04 * cv2.arcLength(c, True), True)
    if len(approx) == 4:
        (x, y, w, h) = cv2.boundingRect(approx)
        ar = w / float(h)
        shape = True if ar >= 0.95 and ar <= 1.05 else False
    return shape


def detect_code(i):
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
        #print(maxi,ind)
        #print(cnts[h[0][ind][-1]])
        if ind and maxi:
            if shape(cnts[h[0][ind][-1]]) != 'h' and shape(
                    cnts[h[0][h[0][ind][-1]][-1]]) != 'h':
                cv2.drawContours(j, [cnts[h[0][ind][-1]]], -1, (0, 0, 255), 2)
                cv2.drawContours(j, [cnts[h[0][h[0][ind][-1]][-1]]], -1,
                                 (0, 255, 0), 2)
                cv2.imshow('code', j)
            #cv2.waitKey(0)
    except:
        pass
    cv2.imshow('gray', t)


'''i=cv2.imread('pic2.png')
detect_code(i)'''
