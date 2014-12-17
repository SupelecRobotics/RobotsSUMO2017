# -*- coding: utf-8 -*-
"""
Created on Wed Dec 17 09:26:47 2014

@author: Darkpudding
"""

import cv2

class ShapeDetection:

    # used in cv2.createTrackBar
    @staticmethod
    def nothing(x):
        pass    
    
    @staticmethod    
    def runImage(imgOriginal):
           
        cv2.namedWindow('Control') # create a window called "Control"
        
        # Create trackbars in "Control" window
        cv2.createTrackbar("Precision", "Control", 5, 10, ShapeDetection.nothing);       
        cv2.createTrackbar("i", "Control", 28,255, ShapeDetection.nothing);
        cv2.createTrackbar("t1", "Control", 0,255, ShapeDetection.nothing);
        cv2.createTrackbar("t2", "Control", 28,255, ShapeDetection.nothing);                
        
        while True:         
            
            p = cv2.getTrackbarPos("Precision", "Control")+1
            i = cv2.getTrackbarPos("i", "Control")
            t1 = cv2.getTrackbarPos("t1", "Control")
            t2 = cv2.getTrackbarPos("t2", "Control")
                
            # create image of shapes by gradient method
            imgShape = cv2.morphologyEx(imgOriginal, cv2.MORPH_GRADIENT, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (p, p)))
            imgShape = cv2.bilateralFilter(imgShape,9,75,75)
            
            # convert into grayscale 
            imgShape = cv2.cvtColor(imgShape, cv2.COLOR_BGR2GRAY)
            # filtre -> denosing
            imgShape = cv2.bilateralFilter(imgShape, 11, 17, 17)
            # find edges
            imgT = cv2.Canny(imgShape, t1, t2)
            # imgShape = cv2.fastNlMeansDenoising(imgShape)  # trop lent
                      
            # threshold
            #_, imgT = cv2.threshold(imgShape, i, 255, cv2.THRESH_BINARY)                        
            
            imgContours = imgT.copy()
            contours, hierarchy = cv2.findContours(imgContours,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)            
            imgContours = imgOriginal.copy()            
            cv2.drawContours(imgContours, contours, -1, (0,255,0), 2)
            
            cv2.imshow("Contours", imgContours)
            cv2.imshow("thresh", imgT);
            cv2.imshow("Image of shapes", imgShape); # show the image of shapes
            cv2.imshow("Original", imgOriginal); # show the original image
        
            if cv2.waitKey(30) == 27: # wait for 'esc' key press for 30ms. If 'esc' key is pressed, break loop
                print("esc key is pressed by user")
                break
        
        # When everything done, release the windows
        cv2.destroyAllWindows()