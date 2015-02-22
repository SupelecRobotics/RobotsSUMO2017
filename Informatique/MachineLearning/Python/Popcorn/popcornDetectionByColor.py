import numpy as np
import cv2

def nothing(x):
    pass

cv2.namedWindow('Saturation')
cv2.createTrackbar('min', 'Saturation', 0, 255, nothing)
cv2.createTrackbar('max', 'Saturation', 0, 255, nothing)

img = cv2.imread('tablePict2.JPG') #Ouverture de l'image
end = False

while(not end):
    
    hsvMin = np.array([0, cv2.getTrackbarPos('min', 'Saturation'), 0])
    hsvMax = np.array([180, cv2.getTrackbarPos('max', 'Saturation'), 255])

    mask = cv2.inRange(img, hsvMin, hsvMax)

    cv2.imshow('Result', mask)
    
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        end = True

cv2.destroyAllWindows()
