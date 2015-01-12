# Programme qui essaie de retrouver l'escalier dans l'image globale de la table,
# en se basant sur une photo de l'escalier seul

# (Pas encore au point)

import numpy as np
import cv2

#Juste une fonction vide, parce que createTrackbar attend un callback en argument
def nothing(x):
    pass

img = cv2.imread('table_small.JPG') #Ouverture de l'image de la table
feature = cv2.imread('escalier_only.jpg') #Ouverture de l'image de l'escalier
orb = cv2.ORB()

kpImg,desImg = orb.detectAndCompute(img, None)
kpFeat,desFeat = orb.detectAndCompute(feature, None)

end = False

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(desFeat,desImg)

# Dessin de petits cercles autours des points qui "collent" entre les deux images
for mat in matches:
    imgIndex = mat.queryIdx
    featIndex = mat.trainIdx

    (x,y) = kpImg[imgIndex].pt

    cv2.circle(img, (int(x),int(y)), 4, (255, 0, 0), 1)


cv2.imshow('Object detection', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
