import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('Noisy.png',0) 
#img = cv2.imread('Blob003.bmp',0)

# Show image
cv2.imshow('Original', img)

kernel = np.ones((3,3),np.uint8)

ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
erosion  = cv2.erode(thresh1,kernel,iterations=1)
dilation = cv2.dilate(erosion,kernel,iterations=3)
dilation = cv2.erode(dilation,kernel,iterations=1)
dilation = cv2.dilate(dilation,kernel,iterations=3)
dilation = cv2.erode(dilation,kernel,iterations=1)
dilation = cv2.dilate(dilation,kernel,iterations=2)
ilation = cv2.erode(dilation,kernel,iterations=1)
dilation = cv2.dilate(dilation,kernel,iterations=2)

# Show image
cv2.imshow('Limpia', dilation)


cv2.waitKey(0)
cv2.destroyAllWindows()
