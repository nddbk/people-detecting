import numpy as np
import cv2
import Person

cap = cv2.VideoCapture('vtest.avi')

w = cap.get(3)
h = cap.get(4)
mx = int(w - 400)
my = int(h - 24)

areaTH = 500
count = 0

fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=True)
kernelOp = np.ones((15, 15), np.uint8)
kernelCl = np.ones((1, 1), np.uint8)


max_p_age = 5
pid = 1
font = cv2.FONT_HERSHEY_SIMPLEX

while(cap.isOpened()):
    ret, frame = cap.read()

    if ret is False:
        break

    k = cv2.waitKey(30)
    if k == 27:
            break

    fgmask = fgbg.apply(frame)
    people = []
    try:

        ret, thresh1 = cv2.threshold(fgmask, 200, 255, cv2.THRESH_BINARY)

        mask = cv2.morphologyEx(thresh1, cv2.MORPH_OPEN, kernelOp)
        mask = cv2.morphologyEx(thresh1, cv2.MORPH_CLOSE, kernelCl)

    except IOError as e:
        print('IO Error:')
        print(e)
        print('EOF')
        break

    except ValueError as e:
        print('Value error:')
        print(e)
        print('EOF')
        break

    _, contour0, hierachy = cv2.findContours(
        mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_NONE
    )
    for cnt in contour0:
        area = cv2.contourArea(cnt)
        if area > areaTH:
            M = cv2.moments(cnt)
            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])
            x, y, w, h = cv2.boundingRect(cnt)

            new = True
            for i in people:
                if abs(x - i.getX()) <= w and abs(y - i.getY()) <= h:
                    new = False
                    i.updateCoords(cx, cy)
                    break
            if new is True:
                p = Person.MyPerson(pid, cx, cy, max_p_age)
                people.append(p)
                pid += 1

            img = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    for i in people:
        if len(i.getTracks()) >= 2:
            pts = np.array(i.getTracks(), np.int32)
            pts = pts.reshape((-1, 1, 2))
            frame = cv2.polylines(frame, [pts], False, i.getRGB())

    count = len(people)
    text = 'People detected: ' + str(count)
    cv2.putText(
        frame,
        text,
        (mx, my),
        font,
        1,
        (255, 255, 255),
        1,
        cv2.LINE_AA
    )
    cv2.imshow('Frame', frame)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
