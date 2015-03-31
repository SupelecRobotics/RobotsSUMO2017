# Programme qui tournera sur chacun des 3 RasPi/balises autour de la map
# Il lit le flux vidéo, reconnaît les objets importants et envoie leurs coordonnées (plus éventuellement d'autres infos) au robot

import numpy as np
import cv2
import PerspectiveTransformer
import CameraUndistorter

def drawCircleProj(event,x,y,flags,param):
    if event == cv2.EVENT_MOUSEMOVE:
        dst = perspectiveTransformer.transform(np.float32([[x,y]]).reshape(-1,1,2))
        final[:] = table
        cv2.circle(final,(int(dst[0][0][0]),int(dst[0][0][1])), 4, (0, 0, 255), 2)

undistorter = CameraUndistorter.CameraUndistorter()
undistorter.loadParam()

cap = cv2.VideoCapture('http://10.13.152.226:8554/') #Ouverture de la caméra
end = False

perspectiveTransformer = PerspectiveTransformer.PerspectiveTransformer()
perspectiveTransformer.loadParamFromFile()

table = cv2.imread('schema_table.png')
final = table.copy()
cv2.namedWindow('Cam')
cv2.setMouseCallback('Cam',drawCircleProj)

while(cap.isOpened() and not end):
    ret,frame = cap.read()

    if(ret):
        #frame = undistorter.undistort(frame)

        cv2.imshow('Cam',frame)
        cv2.imshow('Final', final)

    if(cv2.waitKey(1) & 0xFF == ord('q')):
        end = True

cap.release()
cv2.destroyAllWindows()
