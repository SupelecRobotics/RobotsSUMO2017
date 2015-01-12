# Programme qui ne sélectionne qu'une certaine étendue de couleurs dans l'image
# Seuls sont affichés les pixels dont les valeurs HSV (Hue Saturation Value)
# sont comprises entre certaines valeurs, définies par les trackbars

# Attention, par défaut, toutes les trackbars sont à zéro, mettez les "max" tout
# à droite pour afficher l'image complète

import numpy as np
import cv2

#Juste une fonction vide, parce que createTrackbar attend un callback en argument
def nothing(x):
    pass

img = cv2.imread('DSC00384.JPG') #Ouverture de l'image
end = False

cv2.namedWindow('Color Detection')

#Création des trackbars
Hmin_tb = cv2.createTrackbar('Hmin', 'Color Detection', 0, 179, nothing)
Smin_tb = cv2.createTrackbar('Smin', 'Color Detection', 0, 255, nothing)
Vmin_tb = cv2.createTrackbar('Vmin', 'Color Detection', 0, 255, nothing)
Hmax_tb = cv2.createTrackbar('Hmax', 'Color Detection', 0, 179, nothing)
Smax_tb = cv2.createTrackbar('Smax', 'Color Detection', 0, 255, nothing)
Vmax_tb = cv2.createTrackbar('Vmax', 'Color Detection', 0, 255, nothing)

while(not end):

    #Récupération des valeurs des trackbars
    Hmin = cv2.getTrackbarPos('Hmin', 'Color Detection')
    Smin = cv2.getTrackbarPos('Smin', 'Color Detection')
    Vmin = cv2.getTrackbarPos('Vmin', 'Color Detection')

    Hmax = cv2.getTrackbarPos('Hmax', 'Color Detection')
    Smax = cv2.getTrackbarPos('Smax', 'Color Detection')
    Vmax = cv2.getTrackbarPos('Vmax', 'Color Detection')

    #Limage de base est codée en RGB (ou BGR plutôt), on la convertit en HSV
    hsvImg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    #On crée un masque à partir des zones de l'image qui sont dans la bonne étendue de couleurs
    color_l = np.array([Hmin,Smin,Vmin])
    color_h = np.array([Hmax,Smax,Vmax])
    mask = cv2.inRange(hsvImg, color_l, color_h)

    #On retire de l'image tout ce qui n'est pas de la bonne couleur
    cropped = cv2.bitwise_and(img, img, mask = mask)
        
    cv2.imshow('Color Detection', cropped) #Affichage du résultat
        
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        end = True

cv2.destroyAllWindows()
