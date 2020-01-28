import cv2
from numpy import int0


def center(c):
    shape = False
    approx = cv2.approxPolyDP(c, 0.04 * cv2.arcLength(c, True), True)
    cx, cy = 0, 0
    if len(approx) == 4:
        x, y, w, h = cv2.boundingRect(approx)
        if x < 10:
            x = 10
        if y < 10:
            y = 10
        x1 = int(x + w)
        y1 = int(y + h)
        cx = int(x + w / 2)
        cy = int(y + h / 2)
        box = [(x, y), (x1, y), (x1, y1), (x, y1)]
        shape = "s"
    elif len(approx) == 3:
        try:
            m = cv2.moments(approx)
            cx = int(m["m10"] / m["m00"])
            cy = int(m["m01"] / m["m00"])
        except ZeroDivisionError:
            pass
        shape = "t"
    elif len(approx) == 8:
        try:
            m = cv2.moments(approx)
            cx = int(m["m10"] / m["m00"])
            cy = int(m["m01"] / m["m00"])
        except ZeroDivisionError:
            pass
        shape = "c"
    if len(approx) != 4:
        return [shape, (cx, cy)]
    else:
        return [shape, (cx, cy), box]


def detect(image, popo):
    (l, w) = image.shape[:2]
    j = image.copy()
    x_min,y_min=0,0
    if popo != False:
        x_min = popo[0][0]
        y_min = popo[1][0]
        image = image[popo[0][0] : popo[0][1], popo[1][0] : popo[1][1]]
    img_2 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, threshold = cv2.threshold(
        img_2, 127, 255, cv2.THRESH_BINARY
    )  # add dynamic thresh
    #cv2.circle(j, (w // 2, l // 2), 5, (255, 255, 255), 1)
    cnts, h = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE,)
    ind = []
    if type(h) != type(None):
        for n, i in enumerate(h[0]):
            # if i[0] == i[1] == i[2] == -1:
            ind.append(n)
        for m in ind:
            out = center(cnts[h[0][h[0][m][-1]][-1]])
            if out[0] == "s":
                inside = center(cnts[h[0][m][-1]])
                if inside[0] == "c":
                    this = center(cnts[m])
                    if this[0] == "t":
                        #box1 = int0(out[2])
                        #cv2.line(j, (w // 2, l // 2), this[1], (0, 0, 255), 1)
                        #cv2.drawContours(j, [box1], -1, (0, 0, 255), 1)
                        popo = [
                            (x_min + out[2][0][1] - 10, x_min + out[2][2][1] + 10),
                            (y_min + out[2][0][0] - 10, y_min + out[2][2][0] + 10),
                        ]
                        #cv2.circle(image, this[1], 10, (0, 0, 255), 1)
                        #cv2.circle(j, this[1], 10, (0, 0, 255), 1)
    else:
        popo = False

    cv2.imshow("Full", j)
    cv2.imshow("Small", image)
    # add for loop for frames
    # cv2.imshow("thresh",threshold)
    return popo


# detect(img)
