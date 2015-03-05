# Programme qui tournera sur chacun des 3 RasPi/balises autour de la map
# Il lit le flux vidéo, reconnaît les objets importants et envoie leurs coordonnées (plus éventuellement d'autres infos) au robot

import numpy as np
import cv2
import ImageProcessor
import PerspectiveTransformer

def drawCircles(table, points):
    tableWithCircles = table.copy()
    for i in range(0, points.shape[0]):
        cv2.circle(tableWithCircles,(int(points[i][0][0]),int(points[i][0][1])),5,(255,255,255),2)
    return tableWithCircles

cap = cv2.VideoCapture('http://10.13.152.226:8554/') #Ouverture de la caméra
end = False

cylinderFinder = ImageProcessor.CylinderFinder()
cylinderFinder.loadParam()

perspectiveTransformer = PerspectiveTransformer.PerspectiveTransformer()
perspectiveTransformer.loadParamFromFile()

table = cv2.imread('schema_table.png')

while(cap.isOpened() and not end):
    ret,frame = cap.read()

    if(ret):
        hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        cylinderFrameCoords,selectionMask,contours = cylinderFinder.process(hsvFrame)
        
        cylinderTableCoords = perspectiveTransformer.transform(cylinderFrameCoords)
        
        final = drawCircles(table, cylinderTableCoords)

        cv2.imshow('Final', final)

    if(cv2.waitKey(1) & 0xFF == ord('q')):
        end = True

cap.release()
cv2.destroyAllWindows()
