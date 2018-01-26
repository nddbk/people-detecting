import numpy as np
from imutils.object_detection import non_max_suppression
import cv2

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

font = cv2.FONT_HERSHEY_SIMPLEX

cap = cv2.VideoCapture('vtest.avi')

w = cap.get(3)
h = cap.get(4)
mx = int(w - 400)
my = int(h - 24)

while(cap.isOpened()):
    ret, frame = cap.read()

    if ret is False:
        break
    
    k = cv2.waitKey(30) 
    if k == 27:
        break

    rects, weights = hog.detectMultiScale(
        frame,
        winStride=(4, 4), 
        padding=(8, 8), 
        scale=1.05
    )
    for (x, y, w, h) in rects:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

    rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
    pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)
    
    people_detected = 0
    
    for (xA, yA, xB, yB) in pick:
        people_detected += 1
        cv2.rectangle(frame, (xA, yA), (xB, yB), (0, 255, 0), 2)

    text = 'People detected: ' + str(people_detected)
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

cap.release()
cv2.destroyAllWindows()
