import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # convert image to grayscale
    Gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
      
    # modify the data type to 32-bit floating point
    Gray = np.float32(Gray)
      
    # cv2.cornerHarris method
    # img - Input image, it should be grayscale and float32 type.
    # blockSize - It is the size of neighbourhood considered for corner detection
    # ksize - Aperture parameter of Sobel derivative used, must be odd.
    # k - Harris detector free parameter in the equation.
    dest = cv2.cornerHarris(Gray, 4, 3, 0.04)
      
    # Results are marked through the dilated corners
    dest = cv2.dilate(dest, None)
      
    # Reverting back to the original image,
    # with optimal threshold value
    frame[dest > 0.01 * dest.max()]=[255, 0, 0]


    # Display the resulting frame
    cv2.imshow('Ventana',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
