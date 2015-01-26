import numpy as np
import cv2

def nothing(x):
    pass

W_CONTOUR_MIN = 10
H_CONTOUR_MIN = 10

cross = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))

cap = cv2.VideoCapture('http://10.17.152.226:12345') #Ouverture de la caméra
end = False

tableTopViewOriginal = cv2.imread('schema_table.png')

cv2.namedWindow('Colors', cv2.WINDOW_NORMAL)
cv2.namedWindow('Match max', cv2.WINDOW_NORMAL)

refImg = cv2.imread('cylinderReference2.png')
refImg = cv2.cvtColor(refImg, cv2.COLOR_BGR2GRAY)
refContours,_ = cv2.findContours(refImg,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)


#Création des trackbars
cv2.createTrackbar('Hmin', 'Colors', 0, 179, nothing)
cv2.createTrackbar('Hmax', 'Colors', 0, 179, nothing)
cv2.createTrackbar('Smin', 'Colors', 0, 255, nothing)
cv2.createTrackbar('Smax', 'Colors', 0, 255, nothing)
cv2.createTrackbar('Vmin', 'Colors', 0, 255, nothing)
cv2.createTrackbar('Vmax', 'Colors', 0, 255, nothing)
cv2.createTrackbar('MatchMax', 'Match max', 0, 1000, nothing)

# Points de repère sur la video
src_pts = np.float32([(55, 323),(17,370),(443,319),(139,334)]).reshape(-1,1,2)
# Points correspndants sur l'image de la table
dst_pts = np.float32([(0,0),(33,233),(334,79),(84,77)]).reshape(-1,1,2)
# Calcul de la matrice de transformation entre les deux
M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5.0)


while(cap.isOpened() and not end):
    ret,frame = cap.read()

    if(ret):
        hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        color_min = np.array([cv2.getTrackbarPos('Hmin', 'Colors'),
                              cv2.getTrackbarPos('Smin', 'Colors'),
                              cv2.getTrackbarPos('Vmin', 'Colors')])
        
        color_max = np.array([cv2.getTrackbarPos('Hmax', 'Colors'),
                              cv2.getTrackbarPos('Smax', 'Colors'),
                              cv2.getTrackbarPos('Vmax', 'Colors')])
        
        matchMax = cv2.getTrackbarPos('MatchMax', 'Match max')/float(1000)
        

        cropped = cv2.inRange(hsvFrame, color_min, color_max)
        eroded = cv2.erode(cropped, cross)

        erodedSupport = eroded.copy()
        contours,_ = cv2.findContours(erodedSupport,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

        tableTopView = tableTopViewOriginal.copy()

        for cnt in contours:
            x,y,w,h = cv2.boundingRect(cnt)
            if(cv2.matchShapes(cnt, refContours[0], 1, 1) < matchMax and w > W_CONTOUR_MIN and h > H_CONTOUR_MIN):
                cv2.drawContours(frame, [cnt], -1, (255, 0, 0))
                dst = cv2.perspectiveTransform(np.float32([[x,y]]).reshape(-1,1,2),M)
                cv2.circle(tableTopView,(int(dst[0][0][0]),int(dst[0][0][1])), 4, (0, 0, 255), 2)
        
        cv2.imshow('Camera', frame)
        cv2.imshow('Mask', eroded)
        cv2.imshow('Top view', tableTopView)

    if(cv2.waitKey(1) & 0xFF == ord('q')):
        end = True
        
cap.release()
cv2.destroyAllWindows()
