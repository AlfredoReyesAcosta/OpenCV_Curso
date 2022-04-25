import cv2
import numpy as np
#from matplotlib import pyplot as plt

#img = cv2.imread('Noisy.png',0)
img = cv2.imread('Blob003.bmp',0)

kernel = np.ones((3,3),np.uint8)

ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

dilation = cv2.dilate(thresh1,kernel,iterations=1)
erosion = cv2.erode(dilation,kernel,iterations=4)
#erosion = cv2.dilate(erosion,kernel,iterations=3)

cv2.imshow('Ventana', erosion)
##titles = ['Original Image', 'Thresholding (127)',
##            'Dilation', 'Erosion']
##
##images = [img, thresh1, dilation, erosion]
##
##for i in range(4):
##    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
##    plt.title(titles[i])
##    plt.xticks([]),plt.yticks([])
##plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
