# Programme qui projette la position de la souris sur la photo de la table
# (en perspective donc) par rapport à une vue en 2D de la table
# Les points de repère pris comme références pour la transformation de perspective
# sont les deux coins opposés de la table et les deux coins visibles de l'escalier

import numpy as np
import cv2
from matplotlib import pyplot as plt

# Callback appelé à chaque déplacement de la souris
def drawCircleProj(event,x,y,flags,param):
    if event == cv2.EVENT_MOUSEMOVE:
        #Application de la matrice de transformation sur le vecteur position de la souris
        dst = cv2.perspectiveTransform(np.float32([[x,y]]).reshape(-1,1,2),M)

        final[:] = table
        cv2.circle(final,(int(dst[0][0][0]),int(dst[0][0][1])), 4, (0, 0, 255), 2)

img = cv2.imread('table_small.JPG')
table = cv2.imread('schema_table.png')
end = False
cv2.namedWindow('Table')
cv2.setMouseCallback('Table',drawCircleProj)

# Points de repère sur la photo
src_pts = np.float32([(142, 96),(588,87),(125,290),(232,143)]).reshape(-1,1,2)
# Points correspndants sur l'image de la table
dst_pts = np.float32([(0,0),(418,0),(121,424),(121,202)]).reshape(-1,1,2)
# Calcul de la matrice de transformation entre les deux
M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5.0)


final = np.empty_like(table)

while(not end):

    cv2.imshow('Table',img)
    cv2.imshow('Top',final)

    if(cv2.waitKey(1) & 0xFF == ord('q')):
        end = True



cv2.destroyAllWindows()
