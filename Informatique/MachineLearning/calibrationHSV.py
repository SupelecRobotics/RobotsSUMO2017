# Même chose que colorDetectImage, mais avec votre webcam au lieu d'une image fixe

import numpy as np
import cv2

def nothing(x):
    pass

cap = cv2.VideoCapture(0) #Ouverture de la caméra
end = False

cv2.namedWindow('Camera')

#Définition de deux formes géométriques (des croix ici) qui servent aux fonctions erode et dilate
erodeElement = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
dilatedElement = cv2.getStructuringElement(cv2.MORPH_CROSS,(7,7))

#Création des trackbars
Hmin_tb = cv2.createTrackbar('Hmin', 'Camera', 0, 179, nothing)
Hmax_tb = cv2.createTrackbar('Hmax', 'Camera', 0, 179, nothing)
Smin_tb = cv2.createTrackbar('Smin', 'Camera', 0, 255, nothing)
Smax_tb = cv2.createTrackbar('Smax', 'Camera', 0, 255, nothing)
Vmin_tb = cv2.createTrackbar('Vmin', 'Camera', 0, 255, nothing)
Vmax_tb = cv2.createTrackbar('Vmax', 'Camera', 0, 255, nothing)

while(cap.isOpened() and not end):
    ret,frame = cap.read() #Lecture d'une frame de la caméra (ret est un booléen confirmant que la frame a bien été lue)

    #Récupération des valeurs des trackbars
    Hmin = cv2.getTrackbarPos('Hmin', 'Camera')
    Smin = cv2.getTrackbarPos('Smin', 'Camera')
    Vmin = cv2.getTrackbarPos('Vmin', 'Camera')
    Hmax = cv2.getTrackbarPos('Hmax', 'Camera')
    Smax = cv2.getTrackbarPos('Smax', 'Camera')
    Vmax = cv2.getTrackbarPos('Vmax', 'Camera')

    color_l = np.array([Hmin,Smin,Vmin])
    color_h = np.array([Hmax,Smax,Vmax])
    
    if(ret):
        #Limage de base est codée en RGB (ou BGR plutôt), on la convertit en HSV
        hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        #On crée un masque à partir des zones de l'image qui sont dans la bonne étendue de couleurs
        mask = cv2.inRange(hsvFrame, color_l, color_h)
        #On retire de l'image tout ce qui n'est pas de la bonne couleur
        cropped = cv2.bitwise_and(frame, frame, mask = mask)

        #Afffichage du résultat
        cv2.imshow('Camera', cropped)
        
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        end = True
cap.release()
cv2.destroyAllWindows()
