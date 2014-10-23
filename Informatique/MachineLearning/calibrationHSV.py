import numpy as np
import cv2

def nothing(x):
    pass

cap = cv2.VideoCapture(0)
end = False

cv2.namedWindow('Camera')

erodeElement = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
dilatedElement = cv2.getStructuringElement(cv2.MORPH_CROSS,(7,7))

Hmin_tb = cv2.createTrackbar('Hmin', 'Camera', 0, 179, nothing)
Hmax_tb = cv2.createTrackbar('Hmax', 'Camera', 0, 179, nothing)
Smin_tb = cv2.createTrackbar('Smin', 'Camera', 0, 255, nothing)
Smax_tb = cv2.createTrackbar('Smax', 'Camera', 0, 255, nothing)
Vmin_tb = cv2.createTrackbar('Vmin', 'Camera', 0, 255, nothing)
Vmax_tb = cv2.createTrackbar('Vmax', 'Camera', 0, 255, nothing)

while(cap.isOpened() and not end):
    ret,frame = cap.read()

    Hmin = cv2.getTrackbarPos('Hmin', 'Camera')
    Smin = cv2.getTrackbarPos('Smin', 'Camera')
    Vmin = cv2.getTrackbarPos('Vmin', 'Camera')

    Hmax = cv2.getTrackbarPos('Hmax', 'Camera')
    Smax = cv2.getTrackbarPos('Smax', 'Camera')
    Vmax = cv2.getTrackbarPos('Vmax', 'Camera')

    color_l = np.array([Hmin,Smin,Vmin])
    color_h = np.array([Hmax,Smax,Vmax])
    
    if(ret):
        hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsvFrame, color_l, color_h)
        cropped = cv2.bitwise_and(frame, frame, mask = mask)
        
        cv2.imshow('Camera', cropped)
        
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        end = True
cap.release()
cv2.destroyAllWindows()
