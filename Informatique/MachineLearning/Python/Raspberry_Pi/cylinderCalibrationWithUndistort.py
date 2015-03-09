import pickle
import cv2
import numpy as np
import ImageProcessor
import CameraUndistorter

def nothing(x):
    pass

def saveParam(param):
    with open('CylinderFinder.dat', 'w') as file:
        pickler = pickle.Pickler(file)
        pickler.dump(param)

def loadParam():
    with open('CylinderFinder.dat', 'r') as file:
        depickler = pickle.Unpickler(file)
        param = depickler.load()
        return param

def createTrackbars():
    cv2.namedWindow('Colors', cv2.WINDOW_NORMAL)
    cv2.namedWindow('Match max', cv2.WINDOW_NORMAL)
    cv2.createTrackbar('Hmin', 'Colors', 0, 179, nothing)
    cv2.createTrackbar('Hmax', 'Colors', 0, 179, nothing)
    cv2.createTrackbar('Smin', 'Colors', 0, 255, nothing)
    cv2.createTrackbar('Smax', 'Colors', 0, 255, nothing)
    cv2.createTrackbar('Vmin', 'Colors', 0, 255, nothing)
    cv2.createTrackbar('Vmax', 'Colors', 0, 255, nothing)
    cv2.createTrackbar('MatchMax', 'Match max', 0, 1000, nothing)

    cv2.setTrackbarPos('Hmax', 'Colors', 179)
    cv2.setTrackbarPos('Smax', 'Colors', 255)
    cv2.setTrackbarPos('Vmax', 'Colors', 255)

def updateTrackbars(param):
    cv2.setTrackbarPos('Hmin', 'Colors', param["colorMin"][0])
    cv2.setTrackbarPos('Smin', 'Colors', param["colorMin"][1])
    cv2.setTrackbarPos('Vmin', 'Colors', param["colorMin"][2])
    cv2.setTrackbarPos('Hmax', 'Colors', param["colorMax"][0])
    cv2.setTrackbarPos('Smax', 'Colors', param["colorMax"][1])
    cv2.setTrackbarPos('Vmax', 'Colors', param["colorMax"][2])
    cv2.setTrackbarPos('MatchMax', 'Match max', param["matchMax"])

def readParamsFromTrackbars():
    colorMin = np.array([cv2.getTrackbarPos('Hmin', 'Colors'),
                         cv2.getTrackbarPos('Smin', 'Colors'),
                         cv2.getTrackbarPos('Vmin', 'Colors')])
    colorMax = np.array([cv2.getTrackbarPos('Hmax', 'Colors'),
                         cv2.getTrackbarPos('Smax', 'Colors'),
                         cv2.getTrackbarPos('Vmax', 'Colors')])
    matchMax = cv2.getTrackbarPos('MatchMax', 'Match max')
    
    param = {"colorMin":colorMin, "colorMax":colorMax, "matchMax":matchMax}

    return param

def cropFrameAddContours(frame, mask, contours):
    cropped = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.drawContours(cropped, contours, -1, (255, 0, 0))
    return cropped

cap = cv2.VideoCapture('http://10.13.152.226:8554/')
end = False

cylinderFinder = ImageProcessor.CylinderFinder()

undistorter = CameraUndistorter.CameraUndistorter()
undistorter.loadParam()

createTrackbars()

while(cap.isOpened() and not end):
    ret,frame = cap.read()
    param = readParamsFromTrackbars()
    cylinderFinder.setParam(param)

    if(ret):
        frame = undistorter.undistort(frame)
        hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        _,mask,validContours = cylinderFinder.process(hsvFrame)
        finalFrame = cropFrameAddContours(frame, mask, validContours)
        cv2.imshow('Result', finalFrame)
        
        
    key = cv2.waitKey(1) & 0xFF
    if(key == ord('q')):
        end = True
    elif(key == ord('s')):
        saveParam(param)
    elif(key == ord('l')):
        param = loadParam()
        updateTrackbars(param)

cap.release()        
cv2.destroyAllWindows()
