import pickle
import numpy as np
import cv2

class RobotsFinder:

    # Classe qui s'occupe de donner la position sur l'image de la base des robots vus par la caméra
    # Doit être calibrée avant utilisation.

    def __init__(self):

        self.ROBOTS_HEIGHT = 360 #mm
        self.MARK_HEIGHT = 70
        
        self.wMin = 20 #Temporaire
        self.hMin = 20 #Temporaire
        
        self.cross = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))

        refImg = cv2.imread('cylinderReference2.png')
        refImg = cv2.cvtColor(refImg, cv2.COLOR_BGR2GRAY)
        self.refContours = cv2.findContours(refImg,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[0]

        self.param = {}

        self.param["ratioMin"] = 0.8 * float(600) / float(880)
        self.param["ratioMax"] = 1.2 * float(600) / float(880)
        
        self.param["colorMin"] = np.array([0, 0, 0])
        self.param["colorMax"] = np.array([179, 255, 255])
        self.param["matchMax"] = 0

    def setParam(self, param):
        self.param = param
        self.param["ratioMin"] = 0.6 * float(600) / float(880)
        self.param["ratioMax"] = 1.4 * float(600) / float(880)

    def loadParam(self):
        with open('RobotsFinder.dat', 'r') as file:
            depickler = pickle.Unpickler(file)
            self.param = depickler.load()

    def getBasePos(self, x, y, w, h):
        xBase = x + w/2
        yBase = y + h + (float(self.ROBOTS_HEIGHT)/float(self.MARK_HEIGHT)) * h
        return (int(xBase), int(yBase))

    def process(self,frame):

        if(len(self.param["roi"]) >= 3):
            roiMask = np.empty((frame.shape[0], frame.shape[1]), np.uint8)         
            cv2.fillPoly(roiMask, np.array([self.param["roi"]]), (255,255,255))
            frame = cv2.bitwise_and(frame, frame, mask = roiMask)
        
        cropped = cv2.inRange(frame, self.param["colorMin"], self.param["colorMax"])
        eroded = cv2.erode(cropped, self.cross)
        contours,_ = cv2.findContours(eroded.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

        validContours = []
        basesPos = []

        for cnt in contours:
            x,y,w,h = cv2.boundingRect(cnt)
            ratio = float(w) / float(h)
            if(cv2.matchShapes(cnt, self.refContours[0], 1, 1) < self.param["matchMax"]/float(1000) and w > self.wMin and h > self.hMin and ratio > self.param["ratioMin"] and ratio < self.param["ratioMax"]):
                validContours.append(cnt)
                basesPos.append(self.getBasePos(x,y,w,h))

        return basesPos, eroded, validContours
