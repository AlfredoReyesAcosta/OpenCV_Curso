import cv2
import numpy as np

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

cap.set(cv2.CAP_PROP_BRIGHTNESS, 50)
print(cap.get(cv2.CAP_PROP_BRIGHTNESS))



##CAP_PROP_POS_MSEC Current position of the video file in milliseconds.
##CAP_PROP_POS_FRAMES 0-based index of the frame to be decoded/captured next.
##CAP_PROP_POS_AVI_RATIO Relative position of the video file
##CAP_PROP_FRAME_WIDTH Width of the frames in the video stream.
##CAP_PROP_FRAME_HEIGHT Height of the frames in the video stream.
##CAP_PROP_FPS Frame rate.
##CAP_PROP_FOURCC 4-character code of codec.
##CAP_PROP_FRAMEq_COUNT Number of frames in the video file.
##CAP_PROP_FORMAT Format of the Mat objects returned by retrieve() .
##CAP_PROP_MODE Backend-specific value indicating the current capture mode.
##CAP_PROP_BRIGHTNESS Brightness of the image (only for cameras).
##CAP_PROP_CONTRAST Contrast of the image (only for cameras).
##CAP_PROP_SATURATION Saturation of the image (only for cameras).
##CAP_PROP_HUE Hue of the image (only for cameras).
##CAP_PROP_GAIN Gain of the image (only for cameras).
##CAP_PROP_EXPOSURE Exposure (only for cameras).
##CAP_PROP_CONVERT_RGB Boolean flags indicating whether images should be converted to RGB.
##CAP_PROP_WHITE_BALANCE Currently unsupported
##CAP_PROP_RECTIFICATION Rectification flag for stereo cameras (note: only supported by DC1394 v 2.x backend currently)

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
