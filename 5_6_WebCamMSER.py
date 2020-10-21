import cv2
import numpy as np

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
#mser = cv2.MSER_create()
mser = cv2.MSER_create( _min_area = 5000, _max_area = 25000, _max_variation = 1.0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    vis = frame.copy()

    regions, _ = mser.detectRegions(frame)
    hulls = [cv2.convexHull(p.reshape(-1, 1, 2)) for p in regions]
    cv2.polylines(vis, hulls, 1, (0, 255, 0))

    # Display the resulting frame
    cv2.imshow('Ventana',vis)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
