import numpy as np
import cv2
import PerspectiveTransformer
import RobotsFinder

def drawCircles(table, points):
    if(points.size == 0):
        return table
    tableWithCircles = table.copy()
    for i in range(0, points.shape[0]):
        cv2.circle(tableWithCircles,(int(points[i][0][0]),int(points[i][0][1])),5,(255,255,255),2)
    return tableWithCircles

cap = cv2.VideoCapture('http://10.13.152.226:8554/') #Ouverture de la caméra
end = False

robotsFinder = RobotsFinder.RobotsFinder()
robotsFinder.loadParam()

perspectiveTransformer = PerspectiveTransformer.PerspectiveTransformer()
perspectiveTransformer.loadParamFromFile()

table = cv2.imread('schema_table.png')

while(cap.isOpened() and not end):
    ret,frame = cap.read()

    if(ret):
        hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        robotsFrameCoords,selectionMask,contours = robotsFinder.process(hsvFrame)

        
        if(len(robotsFrameCoords) > 0):
            robotsTableCoords = perspectiveTransformer.transform(np.array(robotsFrameCoords, np.float32).reshape(-1,1,2))
            tableWithCircles = drawCircles(table, robotsTableCoords)
            cv2.circle(frame,robotsFrameCoords[0],5,(255,255,255),2)

        cv2.imshow('Cam', frame)
        cv2.imshow('Table', tableWithCircles)

    if(cv2.waitKey(1) & 0xFF == ord('q')):
        end = True

cap.release()
cv2.destroyAllWindows()
