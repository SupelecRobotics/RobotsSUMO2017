# Programme qui est censé dessiner un contour autour tous les objets d'une
# certaine couleur (vert ici)
# Mais ça marche pas encore...

import numpy as np
import cv2

img = cv2.imread('table_small.JPG') #Ouverture de la caméra
end = False

#Définition de deux formes géométriques (des croix ici) qui servent aux fonctions erode et dilate
erodeElement = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
dilatedElement = cv2.getStructuringElement(cv2.MORPH_CROSS,(7,7))

color_l = np.array([37,43,0])
color_h = np.array([97,255,210])

while(not end):
    
    #L'image de base est codée en RGB (ou BGR plutôt), on la convertit en HSV
    hsvFrame = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    #On crée un masque à partir des zones de l'image qui sont dans la bonne étendue de couleurs
    mask = cv2.inRange(hsvFrame, color_l, color_h)
    contours,_ = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img, contours, -1, (0,255,0), 3)

    #Afffichage du résultat
    cv2.imshow('Mask', img)
        
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        end = True
        
cv2.destroyAllWindows()
