import numpy as np
import cv2

cap = cv2.VideoCapture('http://10.13.152.226:8554')

fgbg = cv2.BackgroundSubtractorMOG()

end = False

while(cap.isOpened() and not end):
    ret, frame = cap.read()

    if(ret):
        fgmask = fgbg.apply(frame)
        cv2.imshow('frame',fgmask)
        
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        end = True
        
cap.release()
cv2.destroyAllWindows()
