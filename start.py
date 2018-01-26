import cv2

font = cv2.FONT_HERSHEY_SIMPLEX

cap = cv2.VideoCapture('vtest.avi')

w = cap.get(3)
h = cap.get(4)
mx = int(w - 400)
my = int(h - 24)

avg = None

while(cap.isOpened()):
    ret, frame = cap.read()

    if ret is False:
        break

    k = cv2.waitKey(30)
    if k == 27:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    if avg is None:
        avg = gray.copy().astype("float")
        continue

    cv2.accumulateWeighted(gray, avg, 0.1)
    frameDelta = cv2.absdiff(gray, cv2.convertScaleAbs(avg))
    cv2.imshow('Frame', frameDelta)
    thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.dilate(thresh, None, iterations=2)
    _, contours, _ = cv2.findContours(
        thresh.copy(),
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    people_detected = 0

    for c in contours:
        if cv2.contourArea(c) < 4000:
            continue
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        people_detected += 1

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
