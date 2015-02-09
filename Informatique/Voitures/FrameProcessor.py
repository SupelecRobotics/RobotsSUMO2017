import cv2
import pickle
import numpy as np


class FrameProcessor:

    def __init__(self):
        self.cross = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
        with open('param.dat', 'r') as file:
            depickler = pickle.Unpickler(file)
            self.data = depickler.load()

    def isMarkVisible(self, frame):
        cropped = cv2.inRange(frame, self.data["colorMin"], self.data["colorMax"])
        eroded = cv2.erode(cropped, self.cross)
        contours,_ = cv2.findContours(eroded,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

        foundMark = False

        for cnt in contours:
            x,y,w,h = cv2.boundingRect(cnt)
            if(w > self.data["Wmin"] and h > self.data["Hmin"]  and w < self.data["Wmax"]  and h < self.data["Hmax"] ):
                foundMark = True
                break
            
        return foundMark
        
