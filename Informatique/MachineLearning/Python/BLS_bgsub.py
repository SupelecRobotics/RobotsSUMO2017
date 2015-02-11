import numpy as np
import cv2

def nothing(x):
    pass

cap = cv2.VideoCapture(0) #Ouverture de la caméra
end = False

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))

frameRefPoints = np.float32([(79, 214),(492,243),(542,375),(365,302)]).reshape(-1,1,2)
tableRefPoints = np.float32([(0,0),(210,0),(210,179),(160,129)]).reshape(-1,1,2)
M,_ = cv2.findHomography(frameRefPoints, tableRefPoints, cv2.RANSAC,5.0)

cv2.namedWindow('Trackbars', cv2.WINDOW_NORMAL)

#Création des trackbars
Hmin_tb = cv2.createTrackbar('Hmin', 'Trackbars', 0, 179, nothing)
Hmax_tb = cv2.createTrackbar('Hmax', 'Trackbars', 0, 179, nothing)
Smin_tb = cv2.createTrackbar('Smin', 'Trackbars', 0, 255, nothing)
Smax_tb = cv2.createTrackbar('Smax', 'Trackbars', 0, 255, nothing)
Vmin_tb = cv2.createTrackbar('Vmin', 'Trackbars', 0, 255, nothing)
Vmax_tb = cv2.createTrackbar('Vmax', 'Trackbars', 0, 255, nothing)

cv2.createTrackbar('roi_b', 'Trackbars', 0, 640, nothing)
cv2.createTrackbar('roi_t', 'Trackbars', 0, 640, nothing)

cv2.setTrackbarPos('roi_t', 'Trackbars', 639)
cv2.setTrackbarPos('Hmax', 'Trackbars', 179)
cv2.setTrackbarPos('Smax', 'Trackbars', 255)
cv2.setTrackbarPos('Vmax', 'Trackbars', 255)

while(cap.isOpened() and not end):
    ret,frame = cap.read() #Lecture d'une frame de la caméra (ret est un booléen confirmant que la frame a bien été lue)

    #Récupération des valeurs des trackbars
    Hmin = cv2.getTrackbarPos('Hmin', 'Trackbars')
    Smin = cv2.getTrackbarPos('Smin', 'Trackbars')
    Vmin = cv2.getTrackbarPos('Vmin', 'Trackbars')
    Hmax = cv2.getTrackbarPos('Hmax', 'Trackbars')
    Smax = cv2.getTrackbarPos('Smax', 'Trackbars')
    Vmax = cv2.getTrackbarPos('Vmax', 'Trackbars')
    bottomROI = cv2.getTrackbarPos('roi_b', 'Trackbars')
    topROI = cv2.getTrackbarPos('roi_t', 'Trackbars')

    color_l = np.array([Hmin,Smin,Vmin])
    color_h = np.array([Hmax,Smax,Vmax])

    table = cv2.imread('tableBLS.png')
    
    if(ret):
        frame = frame[bottomROI:topROI,:]

        hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        mask = cv2.inRange(hsvFrame, color_l, color_h)
        mask = cv2.erode(mask, kernel)
        mask = cv2.bitwise_not(mask)

        contours,_ = cv2.findContours(mask.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

        coords = np.empty([0,2],float)

        atLeastOne = False
        for cnt in contours:
            x,y,w,h = cv2.boundingRect(cnt)
            atLeastOne = True
            if(w > 10 and h > 10):
                coords = np.vstack((coords, [x,y + h/2]))
        
        transfCoords = cv2.perspectiveTransform(coords.reshape(-1,1,2),M)

        if atLeastOne:
            for c in transfCoords:
                cv2.circle(table,(int(c[0][0]),int(c[0][1])), 4, (0, 0, 255), 2)

        cropped = cv2.bitwise_and(frame, frame, mask = mask)

        cv2.drawContours(cropped, contours, -1, (255, 0, 0))
        

        #Afffichage du résultat
        cv2.imshow('Camera', cropped)
        cv2.imshow('Table', table)
        
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        end = True
cap.release()
cv2.destroyAllWindows()
