import cv2
import numpy as np
from matplotlib import pyplot as plt

#img = cv2.imread('Noisy.png',0)
img = cv2.imread('Sudoku.jpg')

# convert image to grayscale
Gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  
# modify the data type to 32-bit floating point
Gray = np.float32(Gray)
  
# cv2.cornerHarris method
# img - Input image, it should be grayscale and float32 type.
# blockSize - It is the size of neighbourhood considered for corner detection
# ksize - Aperture parameter of Sobel derivative used, must be odd.
# k - Harris detector free parameter in the equation.
dest = cv2.cornerHarris(Gray, 2, 3, 0.04)
  
# Results are marked through the dilated corners
dest = cv2.dilate(dest, None)
  
# Reverting back to the original image,
# with optimal threshold value
img[dest > 0.01 * dest.max()]=[0, 0, 255]
  
# Show image
cv2.imshow('Image with Borders', img)

# Wait to show it
cv2.waitKey(0)
cv2.destroyAllWindows()
