import numpy as np
import cv2

# loads the image in color
img = cv2.imread('Sudoku.jpg')

# Show image
cv2.imshow('image', img)

# Wait to show it
cv2.waitKey(0)
cv2.destroyAllWindows()
