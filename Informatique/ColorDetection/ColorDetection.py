# -*- coding: utf-8 -*-
"""
Created on Sun Dec 14 19:31:20 2014

@author: Darkpudding
"""

import numpy as np
import cv2

# used in cv2.createTrackBar
def nothing(x):
    pass

cap = cv2.VideoCapture(0) # capture the video from web cam

if  not cap.isOpened():  # if not success, exit program
    print("Cannot open the web cam")
else:
    print("webcam opened")
    
   
cv2.namedWindow('Control') # create a window called "Control"

# Hue, Saturation, Value
iLowH = 0
iHighH = 179

iLowS = 0
iHighS = 255

iLowV = 0
iHighV = 255

# Create trackbars in "Control" window
cv2.createTrackbar("LowH", "Control", iLowH, 179, nothing); # Hue (0 - 179)
cv2.createTrackbar("HighH", "Control", iHighH, 179, nothing);

cv2.createTrackbar("LowS", "Control", iLowS, 255, nothing); # Saturation (0 - 255)
cv2.createTrackbar("HighS", "Control", iHighS, 255, nothing);

cv2.createTrackbar("LowV", "Control", iLowV, 255, nothing); # Value (0 - 255)
cv2.createTrackbar("HighV", "Control", iHighV, 255, nothing);

cv2.createTrackbar("Resolution", "Control", 5, 10, nothing); # erode, dilate size

while True:
    # Capture frame-by-frame
    ret, imgOriginal = cap.read()
    # initialization 
    imgHSV = imgOriginal
    imgThresholded = imgOriginal    
    
    imgHSV = cv2.cvtColor(imgOriginal, cv2.COLOR_BGR2HSV) # Convert the captured frame from BGR to HSV  
    # lowe_HSV= [LowH,LowS,LowV]  upper_HSV = [HighH,HighS,HighV]    
    lower_HSV = np.array([cv2.getTrackbarPos('LowH','Control'),cv2.getTrackbarPos('LowS','Control'),cv2.getTrackbarPos('LowV','Control')])
    upper_HSV = np.array([cv2.getTrackbarPos('HighH','Control'),cv2.getTrackbarPos('HighS','Control'),cv2.getTrackbarPos('HighV','Control')])  
    s = cv2.getTrackbarPos("Resolution", "Control")+1  # erode, dilate size
    
    imgThresholded = cv2.inRange(imgHSV, lower_HSV, upper_HSV) #Threshold the image    
    
    # morphological opening (remove small objects from the foreground)
    imgThresholded = cv2.erode(imgThresholded, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (s, s)) );
    imgThresholded = cv2.dilate(imgThresholded, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (s, s)) ); 

    # morphological closing (fill small holes in the foreground)
    imgThresholded = cv2.dilate(imgThresholded, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (s, s)) ); 
    imgThresholded = cv2.erode(imgThresholded, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (s, s)) );

    cv2.imshow("Thresholded Image", imgThresholded); # show the thresholded image
    cv2.imshow("Original", imgOriginal); # show the original image

    if cv2.waitKey(30) == 27: # wait for 'esc' key press for 30ms. If 'esc' key is pressed, break loop
        print("esc key is pressed by user")
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
