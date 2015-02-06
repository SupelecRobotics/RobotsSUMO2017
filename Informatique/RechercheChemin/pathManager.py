# -*- coding: utf-8 -*-
"""
Created on Thu Jan  8 21:52:30 2015

@author: antoinemarechal
"""
import math
import timeit
import util
from aStar import AStar

class PathManager :
    
    def __init__(self, matrix) :
        
        self.baseMap = matrix
        self.thresholdMap = [[ ]]
        self.setThreshold(0)
        self.path = []
        self.t0 = timeit.default_timer()
        
    def setThreshold(self, threshold) :
        """ threshold : int
            
        """
        self.thresholdMap = [ [ (self.baseMap[x][y] > 0 or self.baseMap[x][y] < -threshold) for y in xrange(len(self.baseMap[x])) ] for x in xrange(len(self.baseMap)) ]
    
    def findPath(self, start, goal) :
        """ start : (float,float), goal : (float,float,float)
        """
        self.printTime()
        a = AStar(start, goal, self.thresholdMap)
        self.printTime()
        a.aStar()
        p = a.buildPath()
        self.printTime()
        #print p
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
                dist += util.dist(self.path[0], self.path[1])
            print dist
        self.printTime()
        
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
                    if not self.thresholdMap[x][y] and util.height((x,y), pointA, pointB) < threshold :
                        return False
            return True
    
    def printTime(self) :
        t = timeit.default_timer()
        print "from pm : " + str(1000*(t - self.t0))
        self.t0 = t
        