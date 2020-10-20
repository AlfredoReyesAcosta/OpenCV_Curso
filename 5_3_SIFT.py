import numpy as np
import cv2

# loads the image in color
img = cv2.imread('Sistemas.jpg')

# Change it to grey
gray=cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)


sift = cv2.xfeatures2d.SIFT_create()
kp = sift.detect(gray,None)
img=cv2.drawKeypoints(gray,kp,img)

# Show image
cv2.imshow('Harris', img)

# Wait to show it
cv2.waitKey(0)
cv2.destroyAllWindows()
