import numpy as np
import cv2

cap = cv2.VideoCapture(0) #Ouverture de la caméra
end = False

while(cap.isOpened() and not end):
    
    ret,frame = cap.read() #Lecture d'une frame de la caméra (ret est un booléen confirmant que la frame a bien été lue)
    
    if(ret):
        sys.stdout.write(frame.tostring())

cap.release()
cv2.destroyAllWindows()
