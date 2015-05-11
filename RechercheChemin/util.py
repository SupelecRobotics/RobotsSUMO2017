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
    dX = float(A[0] - B[0])
    dY = float(A[1] - B[1])
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
        calculates the angle AÔB in radians
    """
    a1 = math.atan2(A[1], A[0])
    a2 = math.atan2(B[1], B[0])
    return a2 - a1

def angle2(A,B,C) :
    """ A, B, C : (float,float) or (int,int)
        result : float
        calculates the angle ABC in radians
    """
    a1 = math.atan2(A[1]-B[1], A[0]-B[0])
    a2 = math.atan2(C[1]-B[1], C[0]-B[0])
    return a2 - a1

def isInPolygon(A, L) :
    """ A : (float,float)
        L : [(float,float)]
        checks whether point A is inside the convex envelope of the list of points L
    """
    if len(L) == 1 :
        return A == L[0]
    
    maxAngle = 0
    minAngle = 0
    for p in L[1:] :
        a = angle2(L[0], A, p)
        a = (a+math.pi) % (2*math.pi) - math.pi
        maxAngle = max(maxAngle, a)
        minAngle = min(minAngle, a)
    return maxAngle - minAngle >= math.pi

