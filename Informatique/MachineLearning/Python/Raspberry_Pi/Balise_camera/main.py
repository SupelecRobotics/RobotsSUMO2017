# Programme qui tournera sur chacun des 3 RasPi/balises autour de la map
# Il lit le flux vidéo, reconnaît les objets importants et envoie leurs coordonnées (plus éventuellement d'autres infos) au robot

import numpy as np
import cv2
import ImageProcessor
import PerspectiveTransformer

cap = cv2.VideoCapture(0) #Ouverture de la caméra
end = False

cylinderFinder = ImageProcessor.CylinderFinder()
cylinderFinder.calibrate()

perspectiveTransformer = PerspectiveTransformer.PerspectiveTransformer()
perspectiveTransformer.calibrate()


while(cap.isOpened() and not end):
    ret,frame = cap.read()

    if(ret):
        hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        cylinderFrameCoords = cylinderFinder.process(hsvFrame)
        
        cylinderTableCoords = perspectiveTransformer.transform(cylinderFrameCoords)

        # TODO : Envoi des coordonnées au robot
        # ...

        cv2.imshow('Camera',frame) #Temporaire

    if(cv2.waitKey(1) & 0xFF == ord('q')):
        end = True

cap.release()
cv2.destroyAllWindows()
