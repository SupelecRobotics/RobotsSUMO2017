# -*- coding: utf-8 -*-
"""
Created on Fri Mar 06 13:37:01 2015

Permet de mettre les images sous le bon format:
    - generer les images d'apprentissage et le sauvegarder
    - generer les labels d'apprentissage et le sauvegarder
    - generer le dictionnaire d'apprentissage et le sauvegarder

@author: Darkpudding
"""

from matplotlib import pyplot as plt
import numpy as np
import cv2

# convertir un tableau 2D (n rows, m columns) en tableau 1D de longueur n*m   
# selon notre convention
def convert(mat):

    res = [0 for i in range(np.shape(mat)[0]*np.shape(mat)[1]*np.shape(mat)[2])]
    indice = 0
    for couleur in range(np.shape(mat)[2]):
        for l in range(np.shape(mat)[0]):
            for c in range(np.shape(mat)[1]):
                res[indice] = mat[l][c][couleur]
                indice +=1
    return res

# lecture des donnees a pertir d'un pickle
def unpickle(file):
    import cPickle
    fo = open(file, 'rb')
    dict = cPickle.load(fo)
    fo.close()
    return dict

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
    num = 1 # numero de l'image source    
    for l in liensSrc:      
        src = cv2.imread(l)     # lecture d'une image source
        tX = 2*src.shape[0]/Nx   # taille des images coupees suivant X
        tY = 2*src.shape[1]/Ny   # taille des images coupees suivant Y
        x = 0; y = 0;           # indices dynamiques pour couper les images         
        for countY in range(Ny):
            for countX in range(Nx):
                temp = src[y:y+tY, x:x+tX]      # image coupee a partir de l.
                x += tX/2                       # incrementation de l'indice x de coupage
                temp = cv2.resize(temp, tailleReduite, interpolation=cv2.INTER_LANCZOS4);   # reduction image
                # numero de l'image coupee: ordre lexicographique countX_countY
                lien = liensDst+'\\'+`num`+'_'+`countY`+'_'+`countX`+'.JPG'    # lien de sauvegarde
                print lien
                cv2.imwrite(lien,temp)
            x = 0; y += tY/2;                   # incrementation de l'indice y de coupage et remise a zero de x
        num += 1
    print '-----Fin de genererImgCrop-----'

# generer "a la main" les labels correspondant aux solutions des donnees.
# Ici dans le cas ou le label est binaire (-1 ou 1)
def genererLabels(liens, lienSave = 'labels.txt'):
    labels = [];
    for l in liens:
        print l
        img = cv2.imread(l)
        cv2.imshow('1',img)
        key = cv2.waitKey(0)
        if key == ord('y'):     # appuyer sur 'y' du clavier pour un label +1
            labels.append(1);
        else:
            labels.append(-1);  # appuyer sur une autre touche du clavier pour un label -1
    np.savetxt('labels.txt',labels,fmt='%i')    # sauvegarde le tableau labels dans 'labels.txt' en integer.
    print '-----Fin de genererLabels-----'

# fonction temporaire lien des images coupees dans mon cas
# args: nombre d'images non coupees, Nx nombre coupage selon x, Ny nombre coupage selon y, lien du dossier contenant les images coupees
def liensImgCrop(N,Nx,Ny,lienDossier='LearningDataCrop'):
    res = []    
    for num in range(1,N+1):
        for countY in range(Ny):
            for countX in range(Nx):
                lien = lienDossier+('\%d' % num)
                lien = lien+'_'+`countY`+'_'+`countX`+'.JPG'
                res.append(lien)
    return res
    
# afficher une image depuis un dict
def afficherImg(lienDict,imgnum):
    img1D = unpickle(lienDict)['data'][imgnum]        
    # traiter le tableau 1D 3072, en image 2D 32*32*(3 couleurs)
    # R_l1 .. R_l32 G_l1 .. G_l32 .. B_l1 .. B_l32  (R_li: composante rouge de la i-ieme ligne de l'image) 
    img2D = [[[0,0,0] for j in range(32)] for i in range(32)]    # creation image noire
    for couleur in range(3):
        indiceDebutCouleur = couleur*1024
        for l in range(32):
            indiceDebutLigne = indiceDebutCouleur + 32*l
            for c in range(32):
                indiceCourant = indiceDebutLigne + c
                img2D[l][c][couleur]=img1D[indiceCourant]
    plt.imshow(img2D)
    return img2D
    
#src = cv2.imread('LearningData\img (10).jpg')
#cv2.imshow("source",src)
#srcHSV = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
#cv2.imshow("HSV",srcHSV)
#dst = cv2.resize(src, (32,32), interpolation=cv2.INTER_LANCZOS4);
#plt.imshow(dst)
#src_crop = src[500:1300, 1300:2100] # [y: y + h, x: x + w]
#dst_crop = cv2.resize(src_crop, (32,32), interpolation=cv2.INTER_LANCZOS4);
#plt.imshow(dst_crop)

# liens des images non coupees des gobelets 
#liensSrc = []
#for i in range(1,49):
#    liensSrc.append('LearningData\img (%d).JPG' % i)
#
#liensDst = 'LearningDataCrop'
#genererImgCrop(liensSrc, liensDst, 2, 2)

# tableau des labels
labels = np.loadtxt('labels.txt')
# liens des images coupees des gobelets 
liensImg = liensImgCrop(48,2,2)
# generer pickle
genererPickle(liensImg,'learningDict',labels)
# affiche 1 image pour verification
#afficherImg('learningDict',0)