import cv2
import numpy as np

cap = cv2.VideoCapture(0)
kernel = np.ones((3,3),np.uint8)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #ret,frame = cv2.threshold(frame,100,255,cv2.THRESH_BINARY)
    #frame = cv2.erode(frame,kernel,iterations=1)
    #frame = cv2.dilate(frame,kernel,iterations=3)

    frame = cv2.Canny(frame,100,200)
    
    # Display the resulting frame
    cv2.imshow('Ventana',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
