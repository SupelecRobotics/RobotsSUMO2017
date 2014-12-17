# -*- coding: utf-8 -*-
"""
Created on Tue Dec 16 21:43:54 2014

@author: Darkpudding
"""

import cv2
import ColorDetection as cd
import ShapeDetection as sd

sd.ShapeDetection.runImage(cv2.imread('test1.jpg'))