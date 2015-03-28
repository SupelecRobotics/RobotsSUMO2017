import cv2
import numpy as np

end = False
cap = cv2.VideoCapture('http://10.13.152.226:8554/')

while(cap.isOpened() and not end):

    ret,frame = cap.read()

    if(ret):
        cv2.imshow('Camera', frame)

    key = cv2.waitKey(1) & 0xFF
    if(key == ord('q')):
        end = True
    elif(key == ord('p')):
        cv2.imwrite('photo.jpg',frame)
        
cap.release()
cv2.destroyAllWindows()
