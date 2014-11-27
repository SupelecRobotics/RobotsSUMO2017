# Programme qui est censé dessiner un contour autour tous les objets d'une
# certaine couleur (vert ici)

import numpy as np
import cv2

img = cv2.imread('table_small.JPG') #Ouverture de la caméra

#Définition d'une forme géométrique (une croix) qui sert à la fonction erode
erodeElement = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))

color_l = np.array([37,43,0])
color_h = np.array([97,255,210])
    
#L'image de base est codée en RGB (ou BGR plutôt), on la convertit en HSV
hsvFrame = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#On crée un masque à partir des zones de l'image qui sont dans la bonne étendue de couleurs
mask = cv2.inRange(hsvFrame, color_l, color_h)

#Affinage (supprime les pixels isolés)
eroded = cv2.erode(mask,erodeElement)

#Recherche et dessin des contours
contours,_ = cv2.findContours(eroded,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (0,255,0), 3)

#Afffichage du résultat
cv2.imshow('Object detection', img)

#Attente d'un appui de touche
cv2.waitKey(0)
        
cv2.destroyAllWindows()
