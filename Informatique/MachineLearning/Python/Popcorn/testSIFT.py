import numpy as np
import cv2

img = cv2.imread('gobelet.jpg')

sift = cv2.SIFT()
kp = sift.detect(img,None)

img2 = cv2.drawKeypoints(img,kp)

cv2.imshow('img2', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
