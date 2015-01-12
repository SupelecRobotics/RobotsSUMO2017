# Programme qui détecte les cylindres verts sur une photo de la table

# Fonctionnement : on vire de l'image tout ce qui n'est pas vert
# (en utlisant les valeurs HSV trouvées via colorDetectImage.py), puis on
# encadre les éléments verts restants par des boîtes. Enfin, on ne trace que
# les boîtes qui ont le bon ratio largeur/hauteur (réglable via les trackbars)

# C'est porc mais ça marche bien pour les cylindres. Pour l'escalier ça risque
# d'être plus compliqué...

import numpy as np
import cv2

#Juste une fonction vide, parce que createTrackbar attend un callback en argument
def nothing(x):
    pass

cv2.namedWindow('Object detection')
img = cv2.imread('table_small.JPG') #Ouverture de l'image
ratioMax = cv2.createTrackbar('Ratio max', 'Object detection', 1, 100, nothing)
ratioMin = cv2.createTrackbar('Ratio min', 'Object detection', 1, 100, nothing)
end = False

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
#cv2.drawContours(img, contours, -1, (0,255,0), 1 )

final = np.empty_like(img)

while(not end):

    final[:] = img
    
    ratioMax = cv2.getTrackbarPos('Ratio max', 'Object detection')/float(100)
    ratioMin = cv2.getTrackbarPos('Ratio min', 'Object detection')/float(100)

    for cnt in contours:
        x,y,w,h = cv2.boundingRect(cnt)
        if w/float(h) < ratioMax and w/float(h) > ratioMin:
            cv2.rectangle(final,(x,y),(x+w,y+h),(0,255,0),2)

    #Afffichage du résultat
    cv2.imshow('Object detection', final)

    if(cv2.waitKey(1) & 0xFF == ord('q')):
        end = True
        
cv2.destroyAllWindows()
