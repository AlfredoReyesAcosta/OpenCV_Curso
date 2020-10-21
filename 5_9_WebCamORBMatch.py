import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# loads the image in grey
img1 = cv2.imread('Portada.jpg', 0)

orb = cv2.ORB_create(nfeatures=500)
kp1, des1 = orb.detectAndCompute(img1, None)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    kp2, des2 = orb.detectAndCompute(frame, None)


    # matcher takes normType, which is set to cv2.NORM_L2 for SIFT and SURF, cv2.NORM_HAMMING for ORB, FAST and BRIEF
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1, des2)
    matches = sorted(matches, key=lambda x: x.distance)

    # draw first 50 matches
    match_img = cv2.drawMatches(img1, kp1, frame, kp2, matches[:50], None)

    # Display the resulting frame
    cv2.imshow('Ventana',match_img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


