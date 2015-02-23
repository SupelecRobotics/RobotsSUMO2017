import cv2
import numpy as np

cap = cv2.VideoCapture(0)
end = False

ret = False

while(cap.isOpened() and not ret):
    ret,background = cap.read()

while(cap.isOpened() and not end):
    ret,frame = cap.read()

    if(ret):
        substracted = cv2.absdiff(frame, background)
        #substracted = cv2.cvtColor(substracted, cv2.COLOR_BGR2GRAY)
        #mask = cv2.inRange(substracted, 20, 255)
        cv2.imshow('Mask', substracted)

    if(cv2.waitKey(1) & 0xFF == ord('q')):
        end = True
        
cap.release()
cv2.destroyAllWindows()
