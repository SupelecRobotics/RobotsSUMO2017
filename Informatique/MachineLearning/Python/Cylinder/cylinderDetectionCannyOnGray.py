import numpy as np
import cv2

#Juste une fonction vide, parce que createTrackbar attend un callback en argument
def nothing(x):
    pass

cv2.namedWindow('Canny')
img = cv2.imread('DSC00384.JPG') #Ouverture de l'image

cv2.createTrackbar('TH1', 'Canny', 0, 255, nothing)
cv2.createTrackbar('TH2', 'Canny', 0, 255, nothing)

end = False

#Définition d'une forme géométrique (une croix) qui sert à la fonction erode
erodeElement = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
    
grayFrame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
grayFrame = cv2.GaussianBlur(grayFrame, (5,5), 0)

while(not end):

    th1 = cv2.getTrackbarPos('TH1', 'Canny')
    th2 = cv2.getTrackbarPos('TH2', 'Canny')

    edges = cv2.Canny(grayFrame, th1, th2)
    
    contours,_ = cv2.findContours(edges.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img, contours, -1, (255, 0, 0))

    cv2.imshow('Edges from Canny', edges)
    cv2.imshow('Contours', img)


    if(cv2.waitKey(1) & 0xFF == ord('q')):
        end = True
        
cv2.destroyAllWindows()
