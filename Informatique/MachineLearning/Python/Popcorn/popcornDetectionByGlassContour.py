# Programme qui essaie de détecter les gobelets de pop-corn remplis, en effectuant une
# détection des contours puis en ne gardant que ceux dont la forme correspond (plus ou moins)
# à un gobelet. La forme du gobelet est donnée par une forme de référence (popcornReference.JPG).

# Ne fonctionne pas. C'est la détection du contour qui foire, car le gobelet est transparent.
# En même temps, quand le gobelet est contre le mur (blanc), même un humain voit difficilement
# le contour du gobelet sur la photo !

import numpy as np
import cv2

def nothing(x):
    pass

erodeElement = cv2.getStructuringElement(cv2.MORPH_CROSS,(2,2))

img = cv2.imread('gobelet.jpg') #Ouverture de l'image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
end = False

ref = cv2.imread('popcornReference.JPG')
ref = cv2.cvtColor(ref, cv2.COLOR_BGR2GRAY)
refContour,_ = cv2.findContours(ref,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cv2.namedWindow('Canny')
cv2.createTrackbar('TH1', 'Canny', 0, 255, nothing)
cv2.createTrackbar('TH2', 'Canny', 0, 255, nothing)

while(not end):

    imgCopy = img.copy()

    th1 = cv2.getTrackbarPos('TH1', 'Canny')
    th2 = cv2.getTrackbarPos('TH2', 'Canny')

    edges = cv2.Canny(gray, th1, th2)
    dilatedEdges = cv2.dilate(edges,erodeElement)

    contours,_ = cv2.findContours(dilatedEdges.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        if(cv2.matchShapes(cnt, refContour[0], 1, 1) < 0.5):
            x,y,w,h = cv2.boundingRect(cnt)
            cv2.rectangle(imgCopy,(x,y),(x+w,y+h),(0,255,0),2)
    
    cv2.imshow('Result', imgCopy)

    if(cv2.waitKey(1) & 0xFF == ord('q')):
        end = True

cv2.destroyAllWindows()
