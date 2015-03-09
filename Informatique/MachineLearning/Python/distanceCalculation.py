import cv2
import numpy as np
import pickle
import ImageProcessor
import CameraUndistorter

FOCAL_LENGHT = 3.6 #mm
REAL_HEIGHT = 70
REAL_WIDTH = 56
SENSOR_HEIGHT = 2.74 #mm
SENSOR_WIDTH = 3.76

def getDistanceH(objH, imageH):
     return FOCAL_LENGHT * REAL_HEIGHT * imageH / (objH * SENSOR_HEIGHT)

def getDistanceW(objW, imageW):
     return FOCAL_LENGHT * REAL_WIDTH * imageW / (objW * SENSOR_WIDTH)


cylinderFinder = ImageProcessor.CylinderFinder()
cylinderFinder.loadParam()

undistorter = CameraUndistorter.CameraUndistorter()
undistorter.loadParam()

end = False
cap = cv2.VideoCapture('http://10.13.152.226:8554/')

okFrame = False

while(cap.isOpened() and not end):

    okFrame,frame = cap.read()

    if(okFrame):
        #dst = undistorter.undistort(frame)
        dst = frame
        imageH = frame.shape[:2][0]
        imageW = frame.shape[:2][1]
        dstHSV = cv2.cvtColor(dst, cv2.COLOR_BGR2HSV)

        _,_,contours = cylinderFinder.process(dstHSV)

        if(len(contours) > 0):
            objH = cv2.boundingRect(contours[0])[3]
            objW = cv2.boundingRect(contours[0])[2]
            distance1 = getDistanceH(objH, imageH)
            distance2 = getDistanceW(objW, imageW)
            print distance2
            cv2.drawContours(dst, contours, -1, (255, 0, 0))
        
        
        cv2.imshow('Undistorted',dst)

    if(cv2.waitKey(1) & 0xFF == ord('q')):
        end = True

cap.release()
cv2.destroyAllWindows()
    
