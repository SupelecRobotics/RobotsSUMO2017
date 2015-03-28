import numpy as np
import cv2
import ImageProcessor
import CameraUndistorter

KNOWN_WIDTH_REAL = 56
KNOWN_WIDTH_PX = 53
KNOWN_DISTANCE = 1400

FOCAL_LENGHT = (KNOWN_WIDTH_PX * KNOWN_DISTANCE) / KNOWN_WIDTH_REAL

def getDistance(perWidth):
    return (KNOWN_WIDTH_REAL * FOCAL_LENGHT) / perWidth

undistorter = CameraUndistorter.CameraUndistorter()
undistorter.loadParam()

cap = cv2.VideoCapture('http://10.13.152.226:8554/') #Ouverture de la caméra
end = False

tennisBallFinder = ImageProcessor.TennisBallFinder()
tennisBallFinder.loadParam()

print "ok"
    
while(cap.isOpened() and not end):
    ret,frame = cap.read()

    if(ret):
        frame = undistorter.undistort(frame)
        hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        _,_,contours = tennisBallFinder.process(hsvFrame)

        if(len(contours) > 0):
            rect = cv2.minAreaRect(contours[0])
            distance = getDistance(rect[1][0])
            cv2.drawContours(frame, contours, -1, (255, 0, 0))
            print distance

        cv2.imshow('Cam', frame)

    if(cv2.waitKey(1) & 0xFF == ord('q')):
        end = True

cap.release()
cv2.destroyAllWindows()
