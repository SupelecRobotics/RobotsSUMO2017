import numpy as np
import cv2

#Juste une fonction vide, parce que createTrackbar attend un callback en argument
def nothing(x):
    pass

cv2.namedWindow('Mask + erode')
cv2.namedWindow('Colors')
cv2.namedWindow('Canny')
img = cv2.imread('DSC00384.JPG') #Ouverture de l'image
cv2.createTrackbar('Hmin', 'Colors', 0, 180, nothing)
cv2.createTrackbar('Hmax', 'Colors', 0, 180, nothing)
cv2.createTrackbar('Smin', 'Colors', 0, 255, nothing)
cv2.createTrackbar('Smax', 'Colors', 0, 255, nothing)
cv2.createTrackbar('Vmin', 'Colors', 0, 255, nothing)
cv2.createTrackbar('Vmax', 'Colors', 0, 255, nothing)

cv2.createTrackbar('TH1', 'Canny', 0, 255, nothing)
cv2.createTrackbar('TH2', 'Canny', 0, 255, nothing)

end = False

#Définition d'une forme géométrique (une croix) qui sert à la fonction erode
erodeElement = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
    
#L'image de base est codée en RGB (ou BGR plutôt), on la convertit en HSV
hsvFrame = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

while(not end):

    hsvMin = np.array([cv2.getTrackbarPos('Hmin', 'Colors'), cv2.getTrackbarPos('Smin', 'Colors'), cv2.getTrackbarPos('Vmin', 'Colors')])
    hsvMax = np.array([cv2.getTrackbarPos('Hmax', 'Colors'), cv2.getTrackbarPos('Smax', 'Colors'), cv2.getTrackbarPos('Vmax', 'Colors')])

    mask = cv2.inRange(hsvFrame, hsvMin, hsvMax)
    eroded = cv2.erode(mask,erodeElement)

    th1 = cv2.getTrackbarPos('TH1', 'Canny')
    th2 = cv2.getTrackbarPos('TH2', 'Canny')

    edges = cv2.Canny(eroded, th1, th2)
    
    contours,_ = cv2.findContours(edges.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    #Afffichage du résultat
    cv2.imshow('Mask + erode', eroded)
    cv2.imshow('Edges from Canny', edges)

    if(cv2.waitKey(1) & 0xFF == ord('q')):
        end = True
        
cv2.destroyAllWindows()
