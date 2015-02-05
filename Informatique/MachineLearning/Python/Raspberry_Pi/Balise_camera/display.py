import numpy as np
import cv2

class DisplayManager:

    def __init__(self):
        self.tablePic = cv2.imread('schema_table.png')

    def displayTable(self, coords):
        finalPic = self.tablePic.copy()

        for crd in coords:
            cv2.circle(finalPic,(int(crd[0][0]),int(crd[0][1])), 4, (0, 0, 255), 2)

        cv2.imshow('Table', finalPic)

    def displayContoursDetection(self, frame, contours, selectionMask):
        croppedFrame = cv2.bitwise_and(frame,frame,mask = selectionMask)
        for cnt in contours:
            cv2.drawContours(croppedFrame, [cnt], -1, (255, 0, 0))

        cv2.imshow('Selection result', croppedFrame)

        
