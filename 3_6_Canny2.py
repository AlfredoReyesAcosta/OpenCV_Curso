import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('Sudoku.jpg',0)

edges = cv2.Canny(img,100,200)


titles = ['Original Image', 'Filtered image',
            'Gx', 'Gy']

images = [img, edges]

for i in range(2):
    plt.subplot(1,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
