#import numpy as np
import cv2

# loads the image in color
img = cv2.imread('Sudoku.jpg')
img[11:30,1:20]=[0, 255,0]# [B,G,R]

# Show image
cv2.imshow('Color', img)
print('Color ', img.shape)

# Change it to grey
gray=cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# Show image
cv2.imshow('Gris', gray)
print('Gris ', gray.shape)

h, w, c = img.shape
#h, w, _ = img.shape
print('width:  ', w)
print('height: ', h)
print('channel:', c)

# Save it in grey as Out
# cv2.imwrite("Out.jpg", gray)

# Wait to show it
cv2.waitKey(0)
cv2.destroyAllWindows()
