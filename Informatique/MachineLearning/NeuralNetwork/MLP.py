# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 19:15:03 2015

Multi Layers Perceptron (MLP) pour les gobelets

@author: Darkpudding
"""

import numpy as np
import cv2

class MLP:
    
    # args: *lienL lien du dict d'apprentissage, *lienT lien du dict de test
    # attributs: *dictL dict d'apprentissage, *test dict de test, *mlp poids et reseau mlp, *param parametres pour l'apprentissage
    def __init__(self, lienL, lienT, hiddenLayerSizes, activateFunc=1, fparam1=1, fparam2=1, maxSteps=100, epsilon=0.001, bp_dw_scale = 0.001, bp_moment_scale = 0): 
        # dictionnaires des echantillons d'apprentissage        
        self.dictL = self.unpickle(lienL)
        # dictionnaire des echantillons de test        
        self.test = self.unpickle(lienT)
        # initialisation de mlp
        layerSizes = np.concatenate([np.concatenate([[3072],hiddenLayerSizes]),[1]])
        self.mlp = cv2.ANN_MLP(layerSizes,activateFunc,fparam1,fparam2)
        # condition d'arret: maxSteps ou epsilon
        criteria = (cv2.TERM_CRITERIA_COUNT | cv2.TERM_CRITERIA_EPS, maxSteps, epsilon)
        # parametres
        # agorithme d'apprentissage: sequential backpropagation algorithm
        self.params = dict( term_crit = criteria, train_method = cv2.ANN_MLP_TRAIN_PARAMS_BACKPROP, bp_dw_scale=bp_dw_scale, bp_moment_scale=bp_moment_scale)

    # lecture des donnees a pertir d'un pickle
    @staticmethod
    def unpickle(file):
        import cPickle
        fo = open(file, 'rb')
        dict = cPickle.load(fo)
        fo.close()
        return dict
        
    #TEST
    
    # apprentissage
    def learn(self):

        import datetime
        
        inputs = np.array(self.dictL['data'], np.float)
        temp = np.array(self.dictL['labels'])       
        outputs = np.array([0 for i in range(temp.size)],np.float)
        # TEST        
        for i in range(temp.size):
            outputs[i]=temp[i]
        sample_weights = np.array([1 for i in range(temp.size)], np.float)  # len(table[:,0])
        a = datetime.datetime.now()        
        iter = self.mlp.train(inputs,outputs,sample_weights,params=self.params)
        b = datetime.datetime.now()
        print "Apprentissage termine!"
        print "Nombre d'iterations: ",iter
        print "Duree",(b-a)
        # retourne le nombre d'iterations effectuees    
        return iter
    
    #TEST    
    
    # sauvegarde de l'etat de mlp (de l'apprentissage)     
    def saveMLP(self, lien='test_mlp.yml'):
        self.mlp.save(lien)

    # charger l'etat d'un mlp depuis un lien
    def loadMLP(self, lien='test_mlp.yml'):
        self.mlp.load(lien)

    # prediction
    def predict(self):
        inputs = np.array(self.test['data'], np.float)
        rien, outputs = self.mlp.predict(inputs)
        return outputs
        
    # calcul des performances
    # TODO
    # compare une donnee de outputs (predite) par rapport au resultat reel 
    def comparer1(self, outputs, num):
        print "Valeur reelle: " + str(self.test['labels'][num])     
        print "Prediction:" + str(outputs[num])
            
    def comparerTout(self, outputs):
        # calcul du nombre d'erreurs directes, on considere un resultat +1 si output>0 et -1 si output<0        
        erreurs = 0        
        for i in range(outputs.size):
            # verifie si la prediction est du meme signe que le label reel (-1 ou +1)
            if np.sign(outputs[i])!=self.test['labels'][i]:
                erreurs += 1
        print "erreurs directes: ", erreurs
        return erreurs
        
    # afficher une image donnee depuis self.dict ou self.test
    def afficherImg(self,dictnum,imgnum):
        
        from matplotlib import pyplot as plt        
        
        if (dictnum>1 or dictnum<0 or imgnum>self.dictL['labels'].size or imgnum<0):
            print "parametres hors du champ" 
            return []
        # si le dictionaire demande est self.test ou self.dictL
        if dictnum==1:
            img1D = self.test['data'][imgnum]
        else:
            img1D = self.dicts['data'][imgnum]
        
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