"""
Face detection using haar feature-based cascade classifiers
"""

# Import required packages:
import cv2
import numpy as np
#from matplotlib import pyplot as plt



def show_detection(image, faces):
    """Draws a rectangle over each detected face"""

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 5)
    return image


# Load image and convert to grayscale:
#img = cv2.imread("test_face_detection.jpg")
img = cv2.imread("Face.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Load cascade classifiers:
cas_alt2 = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
cas_default = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Detect faces:
faces_alt2              = cas_alt2.detectMultiScale(gray)
faces_default           = cas_default.detectMultiScale(gray)

# Draw face detections:
img_faces_alt2 = show_detection(img.copy(),     faces_alt2)
img_faces_default = show_detection(img.copy(),  faces_default)

# Plot the images:
cv2.imshow('Face',img_faces_alt2)
cv2.waitKey(0)  # Waits for a key
cv2.destroyAllWindows()
