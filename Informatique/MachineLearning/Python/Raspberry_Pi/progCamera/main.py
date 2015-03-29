# Programme qui tournera sur chacun des 3 RasPi/balises autour de la map
# Il lit le flux vidéo, reconnaît les objets importants et envoie leurs coordonnées (plus éventuellement d'autres infos) au robot

import numpy as np
import cv2
import ImageProcessor
import PerspectiveTransformer
import CameraUndistorter

import serial
import RPi.GPIO as GPIO
import time

import RaspiBluetooth

#BlueTSer = RaspiBluetooth.bluetoothInit()

undistorter = CameraUndistorter.CameraUndistorter()
undistorter.loadParam()

cap = cv2.VideoCapture("/dev/video0") #Ouverture de la caméra
cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 720)

end = False

cylinderFinder = ImageProcessor.CylinderFinder()
cylinderFinder.loadParam()

perspectiveTransformer = PerspectiveTransformer.PerspectiveTransformer()
perspectiveTransformer.loadParamFromFile()

print cap.isOpened()

while(cap.isOpened() and not end):
    ret,frame = cap.read()

    if(ret):
        frame = undistorter.undistort(frame)
	cv2.imwrite("test.jpg", frame) 
	hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	        	
	cylinderFrameCoords,selectionMask,contours = cylinderFinder.process(hsvFrame)
        
        if(cylinderFrameCoords.size > 0):
            cylinderTableCoords = perspectiveTransformer.transform(cylinderFrameCoords)
	    print str(cylinderTableCoords.tolist())
	    #BlueTSer.write(str(cylinderTableCoords.tolist()))

cap.release()
cv2.destroyAllWindows()
