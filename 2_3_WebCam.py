import cv2
import numpy as np

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

cap.set(CV_CAP_PROP_EXPOSURE, 160)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 120)

# 160  x 120
# 320  x 240
# 640  x 480
# 1280 x 720
# 1280 x 1024

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Display the resulting frame
    cv2.imshow('Ventana',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
