import cv2
import numpy as np
import pickle
import FrameProcessor

frameProcessor = FrameProcessor.FrameProcessor()
cap = cv2.VideoCapture("http://10.17.152.226:12345")

end  = False

while not end:
    ret,frame = cap.read()

    if(ret):
        if(not frameProcessor.isMarkVisible(frame)):
            cv2.imwrite('finish.jpg',frame)
            end = True

cv2.imshow('Finish', frame)
cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()
