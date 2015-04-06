# -*- coding: utf-8 -*-
"""
Created on Thu Jan  8 21:52:30 2015

@author: antoinemarechal
"""

# PATHMANAGER POUR LES NULS
# 1) créer un objet PathManager en précisant la matrice (entiers)
# 2) si besoin, appeler la méthode setThreshold pour préciser les valeurs considérées comme des obstacles
# 3) appeler la méthode findPath en précisant le point de départ et d'arrivée
# 4) le chemin trouvé est l'attribut path

import aStar
import math
import util


class PathManager :
    
    def __init__(self, matrix) :
        """ matrix : [[int]]
            'matrix' represents the grid :
            - positives are always free spaces
            - 0s are always obstacle
            - negatives are either free spaces or obstacle, depending on the threshold
        """
        self.baseMap = matrix       # base integer matrix
        self.thresholdMap = [[ ]]   # bool matrix for use by the AStar class
        self.setThreshold(0)        # default threshold is 0
        self.path = []
        
    def setThreshold(self, threshold) :
        """ threshold : int
            constructs thresholdMap from baseMap : 
            values between 0 and -threshold are obstacles (False), other values are free spaces (True)
        """
        self.thresholdMap = [ [ (self.baseMap[x][y] > 0 or self.baseMap[x][y] < -threshold) for y in xrange(len(self.baseMap[x])) ] for x in xrange(len(self.baseMap)) ]
    
    def findPath(self, start, goal) :
        """ start : (float,float), goal : (float,float,float) or (float,float)
            uses the AStar class to find the shortest path between 'start' and 'goal'
            then simplifies the path to obtain straight lines as long as possible
        """
        if len(goal) == 2 :
            goal = goal + (0,)  # default value of 'goalRadius' is 0
        a = aStar.AStar(start, goal, self.thresholdMap)
        a.aStar()
        p = a.buildPath()
        if p == None :
            self.path == None
        else :
            l = len(p)
            current = l-1
            self.path = [p[current]]
            while current > 0:
                i = 0
                while i+1 < current and not self.isLineClear(p[current], p[i]) :
                    i += 1
                current = i
                self.path.insert(0,p[current])
        
    def isLineClear(self, pointA, pointB) :
        """ pointA, pointB : (float,float)
            returns : bool (line is clear)
            checks there is no obstacle near the segment [pointA,pointB]
        """ 
        threshold = 0.6
        
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
    
    def getPathLength(self) :
        """ returns : float
            sums the length of each segment of 'self.path'
        """
        lastPoint = None
        length = 0
        for x,y in self.path :
            if lastPoint != None :
                length += util.dist(lastPoint, (x,y))
            lastPoint = (x,y)
        return length
    
    def getPathDuration(self, linSpeed, angSpeed) :
        """ linSpeed : float, angSpeed : float
            returns : float
            sums the duration of each segment and each rotation
        """
        lastPoint = None
        lastSegment = None
        duration = 0
        for x,y in self.path :
            if lastPoint != None :
                duration += util.dist(lastPoint, (x,y)) / linSpeed
                dX = x - lastPoint[0]
                dY = y - lastPoint[1]
                if lastSegment != None :
                    a = (180/math.pi) * util.angle(lastSegment, (dX,dY))
                    a = abs(a)
                    if a > 90 :
                        a = 180 - a
                    duration += a / angSpeed
                lastSegment = (dX,dY)
            lastPoint = (x,y)
        return duration




