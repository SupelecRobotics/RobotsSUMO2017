import numpy as np
import cv2

def nothing(x):
    pass

img = cv2.imread('table_small.JPG')
end = False

cv2.namedWindow('Color Detection')

Hmin_tb = cv2.createTrackbar('Hmin', 'Color Detection', 0, 179, nothing)
Smin_tb = cv2.createTrackbar('Smin', 'Color Detection', 0, 255, nothing)
Vmin_tb = cv2.createTrackbar('Vmin', 'Color Detection', 0, 255, nothing)
Hmax_tb = cv2.createTrackbar('Hmax', 'Color Detection', 0, 179, nothing)
Smax_tb = cv2.createTrackbar('Smax', 'Color Detection', 0, 255, nothing)
Vmax_tb = cv2.createTrackbar('Vmax', 'Color Detection', 0, 255, nothing)

while(not end):

    Hmin = cv2.getTrackbarPos('Hmin', 'Color Detection')
    Smin = cv2.getTrackbarPos('Smin', 'Color Detection')
    Vmin = cv2.getTrackbarPos('Vmin', 'Color Detection')

    Hmax = cv2.getTrackbarPos('Hmax', 'Color Detection')
    Smax = cv2.getTrackbarPos('Smax', 'Color Detection')
    Vmax = cv2.getTrackbarPos('Vmax', 'Color Detection')

    color_l = np.array([Hmin,Smin,Vmin])
    color_h = np.array([Hmax,Smax,Vmax])

    hsvImg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    mask = cv2.inRange(hsvImg, color_l, color_h)
    cropped = cv2.bitwise_and(img, img, mask = mask)
        
    cv2.imshow('Color Detection', cropped)
        
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        end = True

cv2.destroyAllWindows()
