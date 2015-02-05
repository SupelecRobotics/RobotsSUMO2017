# Programme qui tournera sur chacun des 3 RasPi/balises autour de la map
# Il lit le flux vidéo, reconnaît les objets importants et envoie leurs coordonnées (plus éventuellement d'autres infos) au robot

import numpy as np
import cv2
import ImageProcessor
import PerspectiveTransformer
import display

cap = cv2.VideoCapture("http://10.17.152.226:12345") #Ouverture de la caméra
end = False

cylinderFinder = ImageProcessor.CylinderFinder()
cylinderFinder.calibrate(cap)

perspectiveTransformer = PerspectiveTransformer.PerspectiveTransformer()
perspectiveTransformer.calibrate()

displayManager = display.DisplayManager()


while(cap.isOpened() and not end):
    ret,frame = cap.read()

    if(ret):
        hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        cylinderFrameCoords,selectionMask,contours = cylinderFinder.process(hsvFrame)
        
        cylinderTableCoords = perspectiveTransformer.transform(cylinderFrameCoords)

        displayManager.displayTable(cylinderTableCoords) #Temporaire

        displayManager.displayContoursDetection(frame, contours, selectionMask) #Temporaire

        # TODO : Envoi des coordonnées au robot
        # ...

    if(cv2.waitKey(1) & 0xFF == ord('q')):
        end = True

cap.release()
cv2.destroyAllWindows()
