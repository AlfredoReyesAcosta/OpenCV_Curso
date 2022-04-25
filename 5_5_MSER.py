import numpy as np
import cv2

# loads the image in color
img = cv2.imread('Sistemas.jpg')


mser = cv2.MSER_create()

vis = img.copy()

regions, _ = mser.detectRegions(img)
hulls = [cv2.convexHull(p.reshape(-1, 1, 2)) for p in regions]
cv2.polylines(vis, hulls, 1, (0, 255, 0))

# Show image
cv2.imshow('MSER', vis)

# Wait to show it
cv2.waitKey(0)
cv2.destroyAllWindows()
