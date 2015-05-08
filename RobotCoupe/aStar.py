# -*- coding: utf-8 -*-
"""
Created on Thu Dec 11 21:34:28 2014

@author: antoinemarechal
"""

# ASTAR POUR LES NULS
# 1) créer un objet AStar en précisant le point de départ, d'arrivée, et la matrice (booléens)
# 2) appeler la méthode aStar : renvoie True si un chemin est trouvé
# 3) appeler la méthode buildPath : renvoie le chemin trouvé (chemin pas-par-pas)

import math
import heapq
import util

class AStar :
    """ Implements the A* algorithm on an unweighed 2D grid with obstacles
    """
    
    def __init__(self, start, goal, matrix) :
        """ start : (float,float) coordinates of the starting point
            goal : (float,float,float) coordinates of the center, and radius, of the target circle
            matrix : [[bool]]
            'matrix' represents the grid : False is an obstacle, True is a free space
            the grid must be bordered with Falses
        """
        
        # variables related to the beginning and the ending of the path
        self.start = start
        self.goal = goal[0:2]
        self.goalRadius = goal[2]
        self.pathEnd = None
        
        self.cellCount = 0  # number of points added to openSet
        
        # matrix registering informations for each point
        height = len(matrix)
        width = len(matrix[0])
        maximum = float('inf')
        self.blockMat = matrix
        self.statusMat = [ [ 1 for y in xrange(width) ] for x in xrange(height) ]       # 1 = inexplored, 0 = in open set, -1 = in closed set
        self.gScoreMat = [ [ maximum for y in xrange(width) ] for x in xrange(height) ]
        self.fScoreMat = [ [ maximum for y in xrange(width) ] for x in xrange(height) ]
        self.prevMat = [ [ None for y in xrange(width) ] for x in xrange(height) ]
        self.openSet = []                                                               # used as a sorted queue
        
        # initialisation of the starting point(s)
        if self.isGoal(self.start) :
            self.pathEnd = self.start   # if starting point fulfills the goal condition
        else :
            x, y = start
            startX = [x] if isinstance(x, int) else [int(x), 1+int(x)]
            startY = [y] if isinstance(y, int) else [int(y), 1+int(y)]
            for x in startX :
                for y in startY :
                    if self.blockMat[x][y] :
                        gScore = util.dist(self.start, (x,y))
                        self.gScoreMat[x][y] = gScore
                        self.fScoreMat[x][y] = gScore + self.heuristicEstimate((x,y))
                        self.addToOpenSet(x,y)
    
    def aStar(self) :
        """ runs the A* algorithm
            returns : bool (success)
        """
        if self.pathEnd != None :   # if starting point fulfills the goal condition
            return True
        
        for x0, y0 in self.lowestCell() :
            if self.isGoal((x0,y0)) :   # the algorithm ends if the goal condition is reached
                self.pathEnd = (x0, y0)
                return True
            self.statusMat[x0][y0] = -1
            for x1, y1 in self.neighbors(x0, y0) :
                newGScore = self.gScoreMat[x0][y0] + util.dist((x0,y0), (x1,y1))
                if self.statusMat[x1][y1] == 1 or self.gScoreMat[x1][y1] > newGScore :
                    self.gScoreMat[x1][y1] = newGScore
                    self.fScoreMat[x1][y1] = newGScore + self.heuristicEstimate((x1,y1))
                    self.prevMat[x1][y1] = (x0,y0)
                    self.addToOpenSet(x1,y1)
        return False
    
    def buildPath(self) :
        """ returns : [(int,int)]
            reconstructs the path found by self.aStar() if it has been run
        """
        if self.pathEnd == None :   # if self.aStar() has not been run
            return None
        elif self.pathEnd == self.start :   # if starting point fulfills the goal condition
            return [self.start]
        else :
            path = [self.pathEnd]
            x, y = self.pathEnd
            while self.prevMat[x][y] != None :
                x, y = self.prevMat[x][y]
                path.insert(0, (x,y))
            if self.start != path[0] :
                path.insert(0, self.start)
            return path
    
    def addToOpenSet(self, x, y) :
        """ x, y : int
            no return
            adds the coordinates (x,y) to self.openSet with the fScore as priority
        """
        self.statusMat[x][y] = 0
        item = (self.fScoreMat[x][y], self.cellCount, x, y) # fScore : priority, cellCount : secondary priority to avoid ties
        heapq.heappush(self.openSet, item)
        self.cellCount += 1
    
    def lowestCell(self) :
        """ yields : (x,y)
            pop items from openSet until finding one that match the current fScore of its coordinates
        """
        #t0 = timeit.default_timer()
        while len(self.openSet) > 0 :
            a, b, x, y = heapq.heappop(self.openSet)
            if self.statusMat[x][y] == 0 and self.fScoreMat[x][y] == a :
                yield (x,y)
    
    def neighbors(self, x0, y0) :
        """ x0, y0 : int
            yields : (int,int)
            finds the neighbors of a point that are not in the closed set, or an obstacle
        """
        for x, y in [(x0,y0+1), (x0,y0-1), (x0+1,y0), (x0-1,y0)] :
            if self.blockMat[x][y] and self.statusMat[x][y] >= 0 :
                yield (x,y)
    
    def heuristicEstimate(self, point) :
        """ point : (int,int)
            returns : float
            the heuristic function is 1.5 times the distance between 'point' and the goal
        """
        return 1.5 * util.dist(point, self.goal)
    
    def isGoal(self, point) :
        """ point : (int,int)
            returns : bool (goal condition reached)
            the goal condition is : being in the circle of center 'self.goal' and radius 'self.goalRadius'
        """
        return round(util.dist(point, self.goal), 3) <= self.goalRadius

