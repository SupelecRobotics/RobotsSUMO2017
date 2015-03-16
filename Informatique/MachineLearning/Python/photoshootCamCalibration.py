import time
import cv2
import numpy as np

end = False
cap = cv2.VideoCapture('http://10.13.152.226:8554/')

count = 0
lastTime = time.time()

while(cap.isOpened() and not end):

    ret,frame = cap.read()

    if(ret):
        if(time.time() - lastTime > 5):
            lastTime = time.time()
            cv2.imwrite('chessboard/shoot_' + str(count) + '.jpg', frame)
            count = count + 1
            cv2.putText(frame, str(count), (300,300), cv2.FONT_HERSHEY_SIMPLEX, 10, (255, 255, 255))
            cv2.imshow('Camera', frame)
            time.sleep(0.5)
        cv2.imshow('Camera', frame)
            
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        end = True
        
cap.release()
cv2.destroyAllWindows()
