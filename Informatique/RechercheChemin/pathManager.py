# -*- coding: utf-8 -*-
"""
Created on Thu Jan  8 21:52:30 2015

@author: antoinemarechal
"""
import math
from aStar import AStar

class PathManager :
    
    def __init__(self, matrix) :
        
        self.baseMap = matrix
        self.thresholdMap = [[ ]]
        self.setThreshold(0)
        self.path = []
        
    def setThreshold(self, threshold) :
        """ threshold : int
            
        """
        self.thresholdMap = [ [ (self.baseMap[x][y] > 0 or self.baseMap[x][y] < -threshold) for y in xrange(len(self.baseMap[x])) ] for x in xrange(len(self.baseMap)) ]
    
    def findPath(self, start, goal) :
        """ start : (float,float), goal : (float,float,float)
        """
        a = AStar(start, goal, self.thresholdMap)
        a.aStar()
        p = a.buildPath()
        print p
        if p == None :
            self.path == None
        else :
            dist = 0
            l = len(p)
            current = l-1
            self.path = [p[current]]
            while current > 0:
                i = 0
                while i+1 < current and not self.isLineClear(p[current], p[i]) :
                    i += 1
                current = i
                self.path.insert(0,p[current])
                dist += math.sqrt( (self.path[0][0]-self.path[1][0])**2 + (self.path[0][1]-self.path[1][1])**2 )
            print dist
    
    def distFromLine(self, point, pointA, pointB) :
        """ point, pointA, pointB : (float,float)
            returns float : square of the orthogonal distance between point and the segment [pointA,pointB]
        """
        x = float(point[0] - pointA[0])
        y = float(point[1] - pointA[1])
        x0 = float(pointB[0] - pointA[0])
        y0 = float(pointB[1] - pointA[1])
        a = x0*x0 + y0*y0
        b = x*y0 - x0*y
        return b*b/a
        
    def isLineClear(self, pointA, pointB) :
        """ pointA, pointB : (float,float)
            returns boolean : whether there is no obstacle near the segment [pointA,pointB]
        """ 
        threshold = 1
        
        if pointA == pointB :
            return True
        else :
            xMin = int(math.floor(min(pointA[0], pointB[0])))
            yMin = int(math.floor(min(pointA[1], pointB[1])))
            xMax = int(math.ceil(max(pointA[0], pointB[0])))
            yMax = int(math.ceil(max(pointA[1], pointB[1])))
            for x in xrange(xMin, 1+xMax) :
                for y in xrange(yMin, 1+yMax) :
                    if not self.thresholdMap[x][y] and self.distFromLine((x,y), pointA, pointB) < threshold :
                        return False
            return True
        