# -*- coding: utf-8 -*-
"""
Created on Fri Mar 06 13:37:01 2015

Permet de mettre les images sous le bon format.

@author: Darkpudding
"""

from matplotlib import pyplot as plt
import numpy as np
import cv2

# convertir un tableau 2D (n rows, m columns) en tableau 1D de longueur n*m   
def convert(mat):
    res = []
    for row in mat:
        res.append(row)
    res = np.concatenate(res)
    return res

# genere et sauvegarde le dictionnaire d'apprentissage ['data','labels'] dans un pickle a partir d'images.
# args: liens des images, lien du pickle de sauvegarde, liste de labels correspondant aux solutions des donnees.
# effectue aussi une reduction de resolution d'image, a 32 pixels par defaut.
def genererPickle(liensImg, lienPickle, labels, tailleReduite=(32,32)):
    data = []   # liste de donnees. chaque donnee est formate en tableau 1D de longueur n*m pour l'apprentissage
    for l in liensImg:
        src = cv2.imread(l) # lecture image
        src = cv2.resize(src, tailleReduite, interpolation=cv2.INTER_LANCZOS4);   # reduction image
        data.append(convert(src))   # ajoute la donne convertie en tableau 1D de longueur n*m dans la liste
    
    # Sauvegarde le dictionnaire dans un fichier pickle
    import pickle
    dictonnaire = { 'data': data, 'labels': labels }
    pickle.dump( dictonnaire, open( lienPickle, "wb" ) )
    print '-----Fin de genererPickle-----'

# genere et sauvegarde des images coupees 
# les images coupees se superposent avec la precedente et suivante de moitie.
# args: liens des images sources, liens des images destinations, Nx nombres d'images suivant x, Ny nombre d'images suivant y.
def genererImgCrop(liensSrc, liensDst, Nx, Ny, tailleReduite=(32,32)):
    for l in liensSrc:      
        src = cv2.imread(l)     # lecture d'une image source
        tX = 2*src.shape[0]/Nx   # taille des images coupees suivant X
        tY = 2*src.shape[1]/Ny   # taille des images coupees suivant Y
        x = 0; y = 0;           # indices dynamiques pour couper les images         
        for countX in range(Nx):
            for countY in range(Ny):
                temp = src[y:y+tY, x:x+tX]      # image coupee a partir de l.
                y += tY/2                       # incrementation de l'indice y de coupage
                temp = cv2.resize(temp, tailleReduite, interpolation=cv2.INTER_LANCZOS4);   # reduction image
                # numero de l'image coupee: ordre lexicographique countX_countY
                lien = liensDst+'\\'+l+'_'+`countX`+'_'+`countY`+'.JPG'    # lien de sauvegarde
                print lien
                cv2.imwrite(lien,temp)
            y = 0; x += tX/2;                   # incrementation de l'indice x de coupage et remise a zero de y
    print '-----Fin de genererImgCrop-----'

#src = cv2.imread('LearningData\img (10).jpg')
#cv2.imshow("source",src)
#srcHSV = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
#cv2.imshow("HSV",srcHSV)
#dst = cv2.resize(src, (32,32), interpolation=cv2.INTER_LANCZOS4);
#plt.imshow(dst)
#src_crop = src[500:1300, 1300:2100] # [y: y + h, x: x + w]
#dst_crop = cv2.resize(src_crop, (32,32), interpolation=cv2.INTER_LANCZOS4);
#plt.imshow(dst_crop)

# liens des images des gobelets
liensSrc = []
for i in range(1,49):
    liensSrc.append('LearningData\img (%d).JPG' % i)

liensDst = 'LearningDataCrop'
genereImgCrop(liensSrc, liensDst, 2, 2)

# labels correspondant aux solutions des donnees.
labels = [1,3,3]