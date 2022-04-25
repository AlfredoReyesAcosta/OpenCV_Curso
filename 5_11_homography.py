import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# loads the image in grey
img1 = cv2.imread('Billete20.jpg')
#img1 = cv2.imread('RoboticaPortada.png')

orb = cv2.ORB_create(nfeatures=1000)
kp1, des1 = orb.detectAndCompute(img1, None)
hT,wT,cT = img1.shape
#print(hT)

while(True):
    # Capture frame-by-frame
    ret, imgWebcam = cap.read()
    frame = imgWebcam.copy()
    
    imgWebcam = cv2.cvtColor(imgWebcam, cv2.COLOR_BGR2GRAY)
    
    kp2, des2 = orb.detectAndCompute(imgWebcam, None)


    # matcher takes normType, which is set to cv2.NORM_L2 for SIFT and SURF, cv2.NORM_HAMMING for ORB, FAST and BRIEF
    #bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    bf = cv2.BFMatcher()
    #matches = bf.match(des1, des2)
    matches = bf.knnMatch(des1,des2,k=2)
    good =[]
    for m,n in matches:
        if m.distance < 0.80 *n.distance:
            good.append(m)
    #print(len(good))
    #matches = sorted(matches, key=lambda x: x.distance)

    match_img = cv2.drawMatches(img1,kp1,frame,kp2,good,None,flags=2)

    if len(good) > 20:
        
        srcPts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
        dstPts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
        matrix, mask = cv2.findHomography(srcPts,dstPts,cv2.RANSAC,5)
        #print(matrix)
 
        pts = np.float32([[0,0],[0,hT],[wT,hT],[wT,0]]).reshape(-1,1,2)
        dst = cv2.perspectiveTransform(pts,matrix)
        img2 = cv2.polylines(frame,[np.int32(dst)],True,(255,0,255),3)
        cv2.imshow('Homography',img2)
    
    # Display the resulting frame
    cv2.imshow('Match',match_img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


