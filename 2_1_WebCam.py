import cv2
#import numpy as np

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Use Flip code 0 to flip vertically 1 to flip horizontally
    #frame = cv2.flip(frame, 1)

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret,frame = cv2.threshold(frame,140,255,cv2.THRESH_BINARY)
    
    # Display the resulting frame
    cv2.imshow('Ventana',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
