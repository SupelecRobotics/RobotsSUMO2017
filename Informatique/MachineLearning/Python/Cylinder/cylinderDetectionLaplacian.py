import numpy as np
import cv2

#Juste une fonction vide, parce que createTrackbar attend un callback en argument
def nothing(x):
    pass

img = cv2.imread('DSC00384.JPG') #Ouverture de l'image


end = False

#Définition d'une forme géométrique (une croix) qui sert à la fonction erode
erodeElement = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
    
grayFrame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

while(not end):


    edges = cv2.Laplacian(grayFrame, cv2.CV_64F)

    cv2.imshow('Laplacian', edges)

    if(cv2.waitKey(1) & 0xFF == ord('q')):
        end = True
        
cv2.destroyAllWindows()
