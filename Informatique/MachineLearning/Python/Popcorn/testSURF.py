import numpy as np
import cv2

img = cv2.imread('gobelet.jpg')

cv2.imshow('Img', img)

surf = cv2.SURF(200)
kp, des = surf.detectAndCompute(img,None)
print len(kp)

img2 = cv2.drawKeypoints(img,kp,None,(255,0,0),4)

cv2.imshow('img2', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
