import numpy as np
import cv2

# loads the image in color
img = cv2.imread('chessboard.png')

# Show image
#cv2.imshow('image1', img)

# Change it to grey
gray=cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

gray = np.float32(gray)
dst = cv2.cornerHarris(gray,2,3,0.04)
#result is dilated for marking the corners, not important
dst = cv2.dilate(dst,None)
# Threshold for an optimal value, it may vary depending on the image.
img[dst>0.01*dst.max()]=[0,0,255]

# Show image
cv2.imshow('Harris', img)

# Wait to show it
cv2.waitKey(0)
cv2.destroyAllWindows()
