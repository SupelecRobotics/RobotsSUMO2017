# -*- coding: utf-8 -*-
"""
Created on Thu Feb  5 22:05:51 2015

@author: antoinemarechal
"""

import math

def dist(A, B) :
    """ A, B : (float,float) or (int,int)
        result : float
        calculates the euclid distance between points A and B
    """
    (A0, A1) = A
    (B0, B1) = B
    dX = float(A0 - B0)
    dY = float(A1 - B1)
    return math.sqrt(dX*dX + dY*dY)

def height(A, B, C) :
    """ A, B, C : (float,float) or (int,int)
        result : float
        calculates the height (squared) of the triangle (ABC) from point A
    """
    x = float(A[0] - C[0])
    y = float(A[1] - C[1])
    x0 = float(B[0] - C[0])
    y0 = float(B[1] - C[1])
    a = x0*x0 + y0*y0
    b = x*y0 - x0*y
    return b*b/a if a != 0 else dist(A, B)

def angle(A,B) :
    """ A, B : (float,float) or (int,int)
        result : float
        calculates the angle AÔB
    """
    a1 = math.atan2(A[1], A[0])
    a2 = math.atan2(B[1], B[0])
    return a2 - a1