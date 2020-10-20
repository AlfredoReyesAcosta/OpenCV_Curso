import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('Noisy.png',0)
#img = cv2.imread('Blob003.bmp',0)

kernel = np.ones((3,3),np.uint8)

ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
erosion  = cv2.erode(thresh1,kernel,iterations=1)
dilation = cv2.dilate(erosion,kernel,iterations=3)
dilation = cv2.erode(dilation,kernel,iterations=1)
dilation = cv2.dilate(dilation,kernel,iterations=3)
dilation = cv2.erode(dilation,kernel,iterations=1)
dilation = cv2.dilate(dilation,kernel,iterations=2)
dilation = cv2.erode(dilation,kernel,iterations=1)
dilation = cv2.dilate(dilation,kernel,iterations=2)

#FilterI = img
FilterI = dilation

sobelx = cv2.Sobel(FilterI,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(FilterI,cv2.CV_64F,0,1,ksize=5)

titles = ['Original Image', 'Filtered image',
            'Gx', 'Gy']

images = [img, FilterI, sobelx, sobely]

for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
