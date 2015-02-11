import cv2
import numpy

cap = cv2.VideoCapture(0)

class FrameProcessor:

    def __init__(self):
        

    def isMarkVisible(self, frame):
        cropped = cv2.inRange(frame, self.colorMin, self.colorMax)
        eroded = cv2.erode(cropped, self.cross)
        contours,_ = cv2.findContours(eroded,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

        foundMark = False

        for cnt in contours:
            x,y,w,h = cv2.boundingRect(cnt)
            if(w > self.wMin and h > self.hMin and w < self.wMax and h < self.hMax):
                foundMark = True
                break
            
        return foundMark
        
