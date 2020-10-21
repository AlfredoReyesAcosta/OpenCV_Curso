import numpy as np
import cv2

# loads the image in color
img = cv2.imread('Sistemas.jpg')

# Change it to grey
gray=cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

orb = cv2.ORB_create(nfeatures=2000)
kp, des = orb.detectAndCompute(gray, None)

kp_img = cv2.drawKeypoints(img, kp, None, color=(0, 255, 0), flags=0)

# Show image
cv2.imshow('ORB', kp_img)

# Wait to show it
cv2.waitKey(0)
cv2.destroyAllWindows()
