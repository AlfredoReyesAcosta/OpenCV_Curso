#import numpy as np
import cv2

# loads the image in color
img = cv2.imread('Sistemas.jpg', 0)

# Show image
cv2.imshow('Nombre de la ventana', img)

# Wait to show it
cv2.waitKey(0)
cv2.destroyAllWindows()
