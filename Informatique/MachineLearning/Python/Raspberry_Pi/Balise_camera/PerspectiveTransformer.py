import numpy as np
import cv2

class PerspectiveTransformer:

    # Classe qui gère la transformation entre les coordonnées d'un point sur une frame
    # et ses coordonnées réelles sur la table.
    # Se calibre en utilisant des points de référence.

    def calibrate(self):
        frameRefPoints = np.float32([(55, 323),(17,370),(443,319),(139,334)]).reshape(-1,1,2)  #Temporaire
        tableRefPoints = np.float32([(0,0),(33,233),(334,79),(84,77)]).reshape(-1,1,2) #Temporaire
        self.M,_ = cv2.findHomography(frameRefPoints, tableRefPoints, cv2.RANSAC,5.0)

    def transform(self, srcPoints):
        return cv2.perspectiveTransform(srcPoints.reshape(-1,1,2),self.M)
