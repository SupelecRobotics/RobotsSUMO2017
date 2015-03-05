import pickle
import numpy as np
import cv2

class PerspectiveTransformer:

    # Classe qui gère la transformation entre les coordonnées d'un point sur une frame
    # et ses coordonnées réelles sur la table.
    # Charge ses paramètres depuis le fichier PerspectiveTransformer.dat, lui-même créé par le programme perspectiveCalibration.py
    

    def loadParamFromFile(self):
        with open('PerspectiveTransformer.dat', 'r') as file:
            depickler = pickle.Unpickler(file)
            data = depickler.load()
            frameRefPoints = np.float32(data[0])
            tableRefPoints = np.float32(data[1])
            self.M,_ = cv2.findHomography(frameRefPoints, tableRefPoints, cv2.RANSAC,5.0)

    def transform(self, srcPoints):
        return cv2.perspectiveTransform(srcPoints.reshape(-1,1,2),self.M)
