import numpy as np
import cv2
import pickle


class CameraUndistorter:

    def __init__(self):
        self.param = ()
        self.refFrameOk = False
    
    def loadParam(self):
        with open('calibParam.dat', 'r') as file:
            depickler = pickle.Unpickler(file)
            self.param = depickler.load()

    def undistort(self, frame):
	
        ret, mtx, dist, rvecs, tvecs = self.param

        if(not self.refFrameOk):
            self.h,self.w = frame.shape[:2]
            self.newcameramtx,self.roi = cv2.getOptimalNewCameraMatrix(mtx,dist,(self.w,self.h),1,(self.w,self.h))
            self.refFrameOk = True

        dst = cv2.undistort(frame, mtx, dist, None, self.newcameramtx)	

	x,y,w,h = self.roi
        dst = dst[y:y+h, x:x+w]

	cv2.imwrite("test.jpg",dst)

        return dst
