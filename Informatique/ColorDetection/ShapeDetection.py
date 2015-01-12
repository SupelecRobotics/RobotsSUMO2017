# -*- coding: utf-8 -*-
"""
Created on Wed Dec 17 09:26:47 2014

@author: Darkpudding
"""

import numpy as np
import cv2

class ShapeDetection:

    # used in cv2.createTrackBar
    @staticmethod
    def nothing(x):
        pass    
    
    @staticmethod    
    def runImage(imgOriginal):
           
        # set up the HSV color of our objects   
        cv2.namedWindow('Reglage Couleur')
        cv2.createTrackbar("LowH", "Reglage Couleur", 0, 179, ShapeDetection.nothing); # Hue (0 - 179)
        cv2.createTrackbar("HighH", "Reglage Couleur", 179, 179, ShapeDetection.nothing);
        cv2.createTrackbar("LowS", "Reglage Couleur", 0, 255, ShapeDetection.nothing); # Saturation (0 - 255)
        cv2.createTrackbar("HighS", "Reglage Couleur", 255, 255, ShapeDetection.nothing);
        cv2.createTrackbar("LowV", "Reglage Couleur", 0, 255, ShapeDetection.nothing); # Value (0 - 255)
        cv2.createTrackbar("HighV", "Reglage Couleur", 255, 255, ShapeDetection.nothing);
        cv2.createTrackbar("Resolution", "Reglage Couleur", 5, 10, ShapeDetection.nothing); # erode, dilate size        
        
        imgThresholded = imgOriginal.copy()       
        
        while True:
            
            imgHSV = cv2.cvtColor(imgOriginal, cv2.COLOR_BGR2HSV) # Convert the captured frame from BGR to HSV  
            # lowe_HSV= [LowH,LowS,LowV]  upper_HSV = [HighH,HighS,HighV]    
            lower_HSV = np.array([cv2.getTrackbarPos('LowH','Reglage Couleur'),cv2.getTrackbarPos('LowS','Reglage Couleur'),cv2.getTrackbarPos('LowV','Reglage Couleur')])
            upper_HSV = np.array([cv2.getTrackbarPos('HighH','Reglage Couleur'),cv2.getTrackbarPos('HighS','Reglage Couleur'),cv2.getTrackbarPos('HighV','Reglage Couleur')])  
            s = cv2.getTrackbarPos("Resolution", "Reglage Couleur")+1  # erode, dilate size          
            
            imgThresholded = cv2.inRange(imgHSV, lower_HSV, upper_HSV) #Threshold the image    
            
            # morphological opening (remove small objects from the foreground)
            imgThresholded = cv2.erode(imgThresholded, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (s, s)) );
            imgThresholded = cv2.dilate(imgThresholded, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (s, s)) ); 
        
            # morphological closing (fill small holecv2.createTrackbar("Resolution", "Control", 5, 10, ColorDetection.nothing);s in the foreground)
            imgThresholded = cv2.dilate(imgThresholded, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (s, s)) ); 
            imgThresholded = cv2.erode(imgThresholded, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (s, s)) );

            cv2.imshow("Thresholded Image", imgThresholded); # show the thresholded image
            cv2.imshow("Original", imgOriginal); # show the original image
        
            if cv2.waitKey(30) == 27: # wait for 'esc' key press for 30ms. If 'esc' key is pressed, break loop
                print("esc key is pressed by user")
                break
        
        # Release the windows
        cv2.destroyAllWindows()

        #----------------------------------------        
        # Shape detection part

        cv2.namedWindow('Control') # create a window called "Control"
        
        # Create trackbars in "Control" window
        cv2.createTrackbar("Precision", "Control", 5, 20, ShapeDetection.nothing);       
        cv2.createTrackbar("i", "Control", 28,255, ShapeDetection.nothing);
        cv2.createTrackbar("canny1", "Control", 0,255, ShapeDetection.nothing);
        cv2.createTrackbar("canny2", "Control", 28,255, ShapeDetection.nothing);                
        
        while True:         
            
            p = cv2.getTrackbarPos("Precision", "Control")+1
            i = cv2.getTrackbarPos("i", "Control")+1
            t1 = cv2.getTrackbarPos("canny1", "Control")
            t2 = cv2.getTrackbarPos("canny2", "Control")
                
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
            
            # Tous les contours
            imgContours = imgT.copy()
            contours,_ = cv2.findContours(imgContours,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)            
            imgContours = imgOriginal.copy()            
            cv2.drawContours(imgContours, contours, -1, (0,255,0), 2)
            # Intersection des cotours avec les zones de couleur choisie
            imgThresholded1 = cv2.dilate(imgThresholded, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (i, i)) )            
            imgContoursColor = cv2.bitwise_and(imgT,imgThresholded1)            
            contoursColor,_ = cv2.findContours(imgContoursColor,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)            
            imgContoursColor = imgOriginal.copy()            
            cv2.drawContours(imgContoursColor, contoursColor, -1, (0,255,0), 2)            
            
            cv2.imshow("Contours", imgContours);
            cv2.imshow("ContoursColor", imgContoursColor);
            # cv2.imshow("thresh", imgT);
            # cv2.imshow("Image of shapes", imgShape); # show the image of shapes
            # cv2.imshow("Original", imgOriginal); # show the original image
        
            if cv2.waitKey(30) == 27: # wait for 'esc' key press for 30ms. If 'esc' key is pressed, break loop
                print("esc key is pressed by user")
                break
        
        # When everything done, release the windows
        cv2.destroyAllWindows()