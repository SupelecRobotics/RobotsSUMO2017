# -*- coding: utf-8 -*-
"""
Created on Thu Dec 11 21:34:28 2014

@author: antoinemarechal
"""

import math
import heapq

class Cell :
    """ Implements one grid cell, with relevants attributes, for use in the AStar class
    """
    count = 0   # number of instances
    BLOCK, VOID, IN_OPEN_SET, IN_CLOSED_SET, REMOVED = xrange(5)    # constants
    
    def __init__(self, x, y, isFree) :
        """ x, y : int, isFree : bool
        """
        self.state = Cell.VOID if isFree else Cell.BLOCK
        self.x = x
        self.y = y
        self.gScore = float('inf')
        self.fScore = float('inf')
        self.origin = None
        self.id = Cell.count
        Cell.count += 1
    
    def __lt__(self, other) :
        """ other : Cell
            returns : bool
            implemented for use in a HeapQueue
            the lower has the lowest fScore : in case of equality, the lower has the lowest id (necessarily different)
        """
        if self.fScore == other.fScore :
            return self.id < other.id
        else :
            return self.fScore < other.fScore
    
    def dist(self, x, y) :
        """ x, y : float
            returns : float
            calculates the euclid distance between the cell and the point of coordinates (x,y)
        """
        dX = float(self.x - x)
        dY = float(self.y - y)
        return math.sqrt(dX*dX + dY*dY)
    
    def neighbors(self) :
        """ yields : (int,int)
        """
        yield (self.x, self.y + 1)
        yield (self.x, self.y - 1)
        yield (self.x + 1, self.y)
        yield (self.x - 1, self.y)
    
    def lineCoords(self, x, y, threshold) :
        """ x, y : int, threshold : float
            yields : (int,int)
        """
        x0 = min(self.x, x)
        y0 = min(self.y, y)
        dX = abs(self.x - x)
        dY = abs(self.y - y)
        a = float(dY)/float(dX)
        b = threshold * math.sqrt(1 + a*a)
        for x in xrange(dX+1) :
            yMin = int(max(0, math.ceil(a*x-b)))
            yMax = int(min(dY, math.floor(a*x+b)))
            for y in xrange(yMin, yMax+1):
                yield (x0+x, y0+y)
    

class AStar :
    """ Implements the A* algorithm on an unweighed 2D grid with obstacles
    """
    
    def __init__(self, start, goal, matrix) :
        """ start, goal : (int,int), matrix : [[int]]
            'matrix' represents the grid : 0 is an obstacle, anything else is a free cell
            the grid must be bordered with 0s
        """
        self.start = start
        self.goal = goal
        self.matrix = [ [ Cell(x, y, matrix[x][y] != 0) for y in xrange(len(matrix[x])) ] for x in xrange(len(matrix)) ]
        self.openSet = []
    
    









