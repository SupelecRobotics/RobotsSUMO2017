# -*- coding: utf-8 -*-
"""
Created on Sat Jan 03 01:38:43 2015

@author: Darkpudding
"""

import numpy as np
import cv2

class SimpleContoursDetection:

    # used in cv2.createTrackBar
    @staticmethod
    def nothing(x):
        pass    
    
    @staticmethod    
    def runImage(imgOriginal):
           
        # set up the HSV color of our objects   
        cv2.namedWindow('Reglage Couleur')
        cv2.createTrackbar("LowH", "Reglage Couleur", 0, 179, SimpleContoursDetection.nothing); # Hue (0 - 179)
        cv2.createTrackbar("HighH", "Reglage Couleur", 179, 179, SimpleContoursDetection.nothing);
        cv2.createTrackbar("LowS", "Reglage Couleur", 0, 255, SimpleContoursDetection.nothing); # Saturation (0 - 255)
        cv2.createTrackbar("HighS", "Reglage Couleur", 255, 255, SimpleContoursDetection.nothing);
        cv2.createTrackbar("LowV", "Reglage Couleur", 0, 255, SimpleContoursDetection.nothing); # Value (0 - 255)
        cv2.createTrackbar("HighV", "Reglage Couleur", 255, 255, SimpleContoursDetection.nothing);
        cv2.createTrackbar("Resolution", "Reglage Couleur", 5, 10, SimpleContoursDetection.nothing); # erode, dilate size        
        
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
        cv2.createTrackbar("e", "Control", 0,200, SimpleContoursDetection.nothing);
        
        while True:         
            
            e = cv2.getTrackbarPos("e", "Control") # TEST
            
            # Contours simple
            imgContours = imgThresholded.copy()
            contours,_ = cv2.findContours(imgContours,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)            
            imgContours = imgOriginal.copy()            
            cv2.drawContours(imgContours, contours, -1, (0,255,0), 2)
            for cnt in contours :
                # 1- polynomial approximation
                # approx = cv2.approxPolyDP(cnt,e+1,True) 
                # cv2.drawContours(imgContours, approx, -1, (0,0,255), 2
                
                # 2- rectangular approximation
                x,y,w,h = cv2.boundingRect(cnt)
                # detection de cylindres superposes
                rect = np.array([[[x,y]],[[x,y+h]],[[x+w,y+h]],[[x+w,y]]])
                score = cv2.matchShapes(cnt,rect,cv2.cv.CV_CONTOURS_MATCH_I1, 0)
                cv2.putText(imgContours,str(score), (x+w/2,y+h/2), cv2.FONT_HERSHEY_PLAIN, 1, 255)
                if score < 0.01*(e+1) :
                    cv2.rectangle(imgContours,(x,y),(x+w,y+h),(0,0,255),2)
                else :
                    cv2.rectangle(imgContours,(x,y+h/2),(x+w/2,y+h),(255,0,0),2)
                    cv2.rectangle(imgContours,(x+w/2,y),(x+w,y+h/2),(255,0,0),2)

            
            cv2.imshow("Contours Simple", imgContours);
            # cv2.imshow("Original", imgOriginal); # show the original image
        
            if cv2.waitKey(30) == 27: # wait for 'esc' key press for 30ms. If 'esc' key is pressed, break loop
                print("esc key is pressed by user")
                break
        
        # When everything done, release the windows
        cv2.destroyAllWindows()