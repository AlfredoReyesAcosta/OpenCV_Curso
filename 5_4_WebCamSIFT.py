import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    sift = cv2.xfeatures2d.SIFT_create()
    #kp = sift.detect(gray,None)
    kp, des = sift.detectAndCompute(gray,None)
    frame=cv2.drawKeypoints(gray,kp,frame)

    # Display the resulting frame
    cv2.imshow('SIFT',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
