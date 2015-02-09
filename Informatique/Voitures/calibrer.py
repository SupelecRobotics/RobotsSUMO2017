import cv2
import numpy as np
import pickle

def nothing(x):
    pass

def saveParam(data):
    with open('param.dat', 'w') as file:
        pickler = pickle.Pickler(file)
        pickler.dump(data)

cap = cv2.VideoCapture("http://10.17.152.226:12345")

end  = False

cross = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))

cv2.namedWindow('Colors', cv2.WINDOW_NORMAL)
cv2.namedWindow('Size', cv2.WINDOW_NORMAL)

cv2.createTrackbar('Hmin', 'Colors', 0, 179, nothing)
cv2.createTrackbar('Hmax', 'Colors', 0, 179, nothing)
cv2.createTrackbar('Smin', 'Colors', 0, 255, nothing)
cv2.createTrackbar('Smax', 'Colors', 0, 255, nothing)
cv2.createTrackbar('Vmin', 'Colors', 0, 255, nothing)
cv2.createTrackbar('Vmax', 'Colors', 0, 255, nothing)
cv2.createTrackbar('Wmin', 'Size', 0, 500, nothing)
cv2.createTrackbar('Hmin', 'Size', 0, 500, nothing)
cv2.createTrackbar('Wmax', 'Size', 0, 500, nothing)
cv2.createTrackbar('Hmax', 'Size', 0, 500, nothing)

while not end:
    ret,frame = cap.read()

    if(ret):

        colorMin = np.array([cv2.getTrackbarPos('Hmin', 'Colors'),
                             cv2.getTrackbarPos('Smin', 'Colors'),
                             cv2.getTrackbarPos('Vmin', 'Colors')])
            
        colorMax = np.array([cv2.getTrackbarPos('Hmax', 'Colors'),
                             cv2.getTrackbarPos('Smax', 'Colors'),
                             cv2.getTrackbarPos('Vmax', 'Colors')])

        data = {"Wmin":cv2.getTrackbarPos('Wmin', 'Size'),
                "Hmin":cv2.getTrackbarPos('Hmin', 'Size'),
                "Wmax":cv2.getTrackbarPos('Wmax', 'Size'),
                "Hmax":cv2.getTrackbarPos('Hmax', 'Size'),
                "colorMin":colorMin,
                "colorMax":colorMax}
        
        mask = cv2.inRange(frame, colorMin, colorMax)
        eroded = cv2.erode(mask, cross)
        contours,_ = cv2.findContours(eroded.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        croppedFrame = cv2.bitwise_and(frame, frame, mask=eroded)

        for cnt in contours:
            x,y,w,h = cv2.boundingRect(cnt)
            if(w > data["Wmin"] and h > data["Hmin"] and w < data["Wmax"] and h < data["Hmax"]):
                cv2.drawContours(croppedFrame, [cnt], -1, (255, 0, 0))

        cv2.imshow('Camera',croppedFrame)

    key = cv2.waitKey(1) & 0xFF

    if(key == ord('q')):
        end = True
    elif(key == ord('s')):
        saveParam(data)

cap.release()
cv2.destroyAllWindows()
        
