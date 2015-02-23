import cv2
import numpy as np

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(6,6))
cap = cv2.VideoCapture('http://10.13.152.226:8554')
end = False

ret = False

while(cap.isOpened() and not ret):
    ret,background = cap.read()

while(cap.isOpened() and not end):
    ret,frame = cap.read()

    if(ret):
        substracted = cv2.absdiff(frame, background)
        substracted = cv2.cvtColor(substracted, cv2.COLOR_BGR2GRAY)
        mask = cv2.inRange(substracted, 20, 255)
        mask = cv2.erode(mask, kernel)
        mask = cv2.dilate(mask, kernel)
        cv2.imshow('Mask', mask)

    if(cv2.waitKey(1) & 0xFF == ord('q')):
        end = True
        
cap.release()
cv2.destroyAllWindows()
