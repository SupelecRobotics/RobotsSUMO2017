import pickle
import numpy as np
import cv2

def nothing(x):
    pass

class TennisBallFinder:

    # Classe qui s'occupe d'extraire les balles de tennis d'une frame donnée et de renvoyer leur position dans l'image.
    # Doit être calibrée avant utilisation.

    def __init__(self):
        
        self.wMin = 20 #Temporaire
        self.hMin = 20 #Temporaire
        self.cross = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))

        refImg = cv2.imread('sphereReference.png')
        refImg = cv2.cvtColor(refImg, cv2.COLOR_BGR2GRAY)
        self.refContours = cv2.findContours(refImg,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[0]

        self.param = {}
        
        self.param["colorMin"] = np.array([0, 0, 0])
        self.param["colorMax"] = np.array([179, 255, 255])
        self.param["matchMax"] = 0

    def setParam(self, param):
        self.param = param

    def loadParam(self):
        with open('TennisBallFinder.dat', 'r') as file:
            depickler = pickle.Unpickler(file)
            self.param = depickler.load()

    def process(self,frame):
        cropped = cv2.inRange(frame, self.param["colorMin"], self.param["colorMax"])
        eroded = cv2.erode(cropped, self.cross)
        contours,_ = cv2.findContours(eroded.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

        ballsCoords = np.empty([0,2],float)
        validContours = []

        for cnt in contours:
            x,y,w,h = cv2.boundingRect(cnt)
            if(cv2.matchShapes(cnt, self.refContours[0], 1, 1) < self.param["matchMax"]/float(1000) and w > self.wMin and h > self.hMin):
                ballsCoords = np.vstack((ballsCoords, [x + w/2,y + h]))
                validContours.append(cnt)

        return ballsCoords, eroded, validContours

class CylinderFinder:

    # Classe qui s'occupe d'extraire les cylindres d'une frame donnée et de renvoyer leur position dans l'image.
    # Doit être calibrée avant utilisation.

    def __init__(self):
        
        self.wMin = 20 #Temporaire
        self.hMin = 20 #Temporaire
        self.cross = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))

        refImg = cv2.imread('cylinderReference3.png')
        refImg = cv2.cvtColor(refImg, cv2.COLOR_BGR2GRAY)
        self.refContours = cv2.findContours(refImg,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[0]

        self.param = {}
        
        self.param["colorMin"] = np.array([0, 0, 0])
        self.param["colorMax"] = np.array([179, 255, 255])
        self.param["matchMax"] = 0

    def setParam(self, param):
        self.param = param

    def loadParam(self):
        with open('CylinderFinder.dat', 'r') as file:
            depickler = pickle.Unpickler(file)
            self.param = depickler.load()

    def process(self,frame):
        cropped = cv2.inRange(frame, self.param["colorMin"], self.param["colorMax"])
        eroded = cv2.erode(cropped, self.cross)
        contours,_ = cv2.findContours(eroded.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

        cylindersCoords = np.empty([0,2],float)
        validContours = []

        for cnt in contours:
            x,y,w,h = cv2.boundingRect(cnt)
            if(cv2.matchShapes(cnt, self.refContours[0], 1, 1) < self.param["matchMax"]/float(1000) and w > self.wMin and h > self.hMin):
                cylindersCoords = np.vstack((cylindersCoords, [x + w/2,y + h]))
                validContours.append(cnt)

        return cylindersCoords, eroded, validContours
