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
# arg: liens des images, lien du pickle de sauvegarde, liste de labels correspondant aux solutions des donnees.
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


src = cv2.imread('LearningData\img (38).jpg')
cv2.imshow("source",src)
srcHSV = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV",srcHSV)
dst = cv2.resize(src, (32,32), interpolation=cv2.INTER_LANCZOS4);
plt.imshow(dst)

# liens des images des gobelets
liensImg = []
for i in range(1,49):
    liensImg.append('LearningData\img (%d).JPG' % i)
    
# labels correspondant aux solutions des donnees.
labels = [1,3,3]