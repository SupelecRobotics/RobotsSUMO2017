import pickle
import numpy as np
import cv2
import display

def nothing(x):
    pass

class CylinderFinder:

    # Classe qui s'occupe d'extraire les cylindres d'une frame donnée et de renvoyer leur position dans l'image.
    # Doit être calibrée avant utilisation.

    def __init__(self):
        
        self.wMin = 10 #Temporaire
        self.hMin = 10 #Temporaire
        self.cross = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))

        refImg = cv2.imread('cylinderReference3.png')
        refImg = cv2.cvtColor(refImg, cv2.COLOR_BGR2GRAY)
        self.refContours = cv2.findContours(refImg,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[0]
        self.colorMin = np.array([0, 0, 119]) #Temporaire
        self.colorMax = np.array([179, 255, 166]) #Temporaire
        self.matchMax = 1000 #Temporaire

    def saveParam(self):
        with open('CylinderFinder.dat', 'w') as file:
            data = {"colorMin":self.colorMin,"colorMax":self.colorMax,"matchMax":self.matchMax}
            pickler = pickle.Pickler(file)
            pickler.dump(data)

    def loadParam(self):
        with open('CylinderFinder.dat', 'r') as file:
            depickler = pickle.Unpickler(file)
            data = depickler.load()

            self.colorMin = data["colorMin"]
            self.colorMax = data["colorMax"]
            self.matchMax = data["matchMax"]

    def updateTrackbars(self):
        cv2.setTrackbarPos('Hmin', 'Colors', self.colorMin[0])
        cv2.setTrackbarPos('Smin', 'Colors', self.colorMin[1])
        cv2.setTrackbarPos('Vmin', 'Colors', self.colorMin[2])
        cv2.setTrackbarPos('Hmax', 'Colors', self.colorMax[0])
        cv2.setTrackbarPos('Smax', 'Colors', self.colorMax[1])
        cv2.setTrackbarPos('Vmax', 'Colors', self.colorMax[2])
        cv2.setTrackbarPos('MatchMax', 'Match max', self.matchMax)

    def calibrate(self, cap):

        displayManager = display.DisplayManager()

        end = False

        cv2.namedWindow('Colors', cv2.WINDOW_NORMAL)
        cv2.namedWindow('Match max', cv2.WINDOW_NORMAL)

        cv2.createTrackbar('Hmin', 'Colors', 0, 179, nothing)
        cv2.createTrackbar('Hmax', 'Colors', 0, 179, nothing)
        cv2.createTrackbar('Smin', 'Colors', 0, 255, nothing)
        cv2.createTrackbar('Smax', 'Colors', 0, 255, nothing)
        cv2.createTrackbar('Vmin', 'Colors', 0, 255, nothing)
        cv2.createTrackbar('Vmax', 'Colors', 0, 255, nothing)
        cv2.createTrackbar('MatchMax', 'Match max', 0, 1000, nothing)

        while(cap.isOpened() and not end):
            ret,frame = cap.read()

            if(ret):
                hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                
                
                self.colorMin = np.array([cv2.getTrackbarPos('Hmin', 'Colors'),
                                      cv2.getTrackbarPos('Smin', 'Colors'),
                                      cv2.getTrackbarPos('Vmin', 'Colors')])
        
                self.colorMax = np.array([cv2.getTrackbarPos('Hmax', 'Colors'),
                                      cv2.getTrackbarPos('Smax', 'Colors'),
                                      cv2.getTrackbarPos('Vmax', 'Colors')])
                self.matchMax = cv2.getTrackbarPos('MatchMax', 'Match max')
                _,mask,contours = self.process(hsvFrame)

                displayManager.displayContoursDetection(frame, contours, mask)

                key = cv2.waitKey(1) & 0xFF

                if(key == ord('q')):
                    end = True
                elif(key == ord('s')):
                     self.saveParam()
                elif(key == ord('l')):
                     self.loadParam()
                     self.updateTrackbars()

        cv2.destroyWindow('Colors')
        cv2.destroyWindow('Match max')
        cv2.destroyWindow('Selection result')

                                


    def process(self,frame):
        cropped = cv2.inRange(frame, self.colorMin, self.colorMax)
        eroded = cv2.erode(cropped, self.cross)
        contours,_ = cv2.findContours(eroded,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

        cylindersCoords = np.empty([0,2],float)
        validContours = []

        for cnt in contours:
            x,y,w,h = cv2.boundingRect(cnt)
            if(cv2.matchShapes(cnt, self.refContours[0], 1, 1) < self.matchMax/float(1000) and w > self.wMin and h > self.hMin):
                cylindersCoords = np.vstack((cylindersCoords, [x,y + h/2]))
                validContours.append(cnt)

        return cylindersCoords, eroded, validContours
