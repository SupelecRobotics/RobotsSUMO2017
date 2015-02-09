# -*- coding: utf-8 -*-
"""
Created on Thu Dec 11 21:34:28 2014

@author: antoinemarechal
"""

import math
import heapq
import util
import timeit

#class Cell :
#    """ Implements one grid cell, with relevants attributes, for use in the AStar class
#    """
#    count = 0   # number of instances
#    INIT, IN_OPEN_SET, IN_CLOSED_SET, REMOVED = xrange(4)    # constants
#    
#    def __init__(self, x, y) :
#        """ x, y : int, isFree : bool
#        """
#        self.state = Cell.INIT
#        self.x = x
#        self.y = y
#        self.gScore = float('inf')
#        self.fScore = float('inf')
#        self.origin = None
#        self.id = Cell.count    # constant
#        Cell.count += 1
#    
#    def __lt__(self, other) :
#        """ other : Cell
#            returns : bool (compares fScore, then gScore (inverse), then id)
#            implemented for use in a HeapQueue
#        """
#        if self.fScore == other.fScore :
#            if self.gScore == other.gScore :
#                return self.id < other.id
#            else :
#                return self.gScore > other.gScore
#        else :
#            return self.fScore < other.fScore
#    
#    def copy(self) :
#        """ returns : Cell (with identical attributes, except id)
#        """
#        new = Cell(self.x, self.y)
#        new.state = self.state
#        new.gScore = self.gScore
#        new.fScore = self.fScore
#        new.origin = self.origin
#        return new
#    
#    def dist(self, x, y) :
#        """ x, y : float
#            returns : float (euclid distance between self and (x,y))
#        """
#        return util.dist((self.x,self.y), (x,y))
#    
#    def neighbors(self) :
#        """ yields : (int,int) (coordinates of side-adjacent cells)
#        """
#        yield (self.x, self.y + 1)
#        yield (self.x, self.y - 1)
#        yield (self.x + 1, self.y)
#        yield (self.x - 1, self.y)
#    

class AStar :
    """ Implements the A* algorithm on an unweighed 2D grid with obstacles
    """
    
    def __init__(self, start, goal, matrix) :
        """ start : (float,float), goal : (float,float,float), matrix : [[bool]]
            'matrix' represents the grid : False is an obstacle, True is a free cell
            the grid must be bordered with Falses
        """
        # for testing :
        self.turnCount = 0
        self.cellCount = 0
        
        self.start = start
        self.goal = goal[0:2]
        self.goalRadius = goal[2]
        self.pathEnd = None
        height = len(matrix)
        width = len(matrix[0])
        maximum = float('inf')
#        t0 = timeit.default_timer()
        self.blockMat = matrix
#        t1 = timeit.default_timer()
#        print 1000 * (t1-t0)
#        t0 = timeit.default_timer()
        self.statusMat = [ [ 1 for y in xrange(width) ] for x in xrange(height) ]    # 1 = inexplored, 0 = in open set, -1 = in closed set
#        t1 = timeit.default_timer()
#        print 1000 * (t1-t0)
#        t0 = timeit.default_timer()
        self.gScoreMat = [ [ maximum for y in xrange(width) ] for x in xrange(height) ]
#        t1 = timeit.default_timer()
#        print 1000 * (t1-t0)
#        t0 = timeit.default_timer()
        self.fScoreMat = [ [ maximum for y in xrange(width) ] for x in xrange(height) ]
#        t1 = timeit.default_timer()
#        print 1000 * (t1-t0)
#        t0 = timeit.default_timer()
        self.prevMat = [ [ None for y in xrange(width) ] for x in xrange(height) ]
#        t1 = timeit.default_timer()
#        print 1000 * (t1-t0)
        self.openSet = []
        for x in xrange(int(math.floor(self.start[0])), 1+int(math.ceil(self.start[0]))) :
            for y in xrange(int(math.floor(self.start[1])), 1+int(math.ceil(self.start[1]))) :
                gScore = util.dist(self.start, (x,y))
                self.gScoreMat[x][y] = gScore
                self.fScoreMat[x][y] = gScore + self.heuristicEstimate((x,y))
                self.addToOpenSet(x,y)
    
    def aStar(self) :
        """ runs the A* algorithm
            returns : bool (success)
        """
        t0 = timeit.default_timer()
        for x0, y0 in self.lowestCell() :
            print 1000*(timeit.default_timer()-t0)
            print "top"
            t0 = timeit.default_timer()
            if self.isGoal((x0,y0)) :    # the algorithm ends if 'goal' is reached
                self.pathEnd = (x0, y0)
                return True
            print 1000*(timeit.default_timer()-t0)
            self.statusMat[x0][y0] = -1
            print 1000*(timeit.default_timer()-t0)
            for x1, y1 in self.neighbors(x0, y0) :
                print str(x1) + ", " + str(y1)
                print 1000*(timeit.default_timer()-t0)
                newGScore = self.gScoreMat[x0][y0] + util.dist((x0,y0), (x1,y1))
                print 1000*(timeit.default_timer()-t0)
                if self.statusMat[x1][y1] == 1 or self.gScoreMat[x1][y1] > newGScore :
                    self.gScoreMat[x1][y1] = newGScore
                    self.fScoreMat[x1][y1] = newGScore + self.heuristicEstimate((x1,y1))
                    self.prevMat[x1][y1] = (x0,y0)
                    self.addToOpenSet(x1,y1)
                print 1000*(timeit.default_timer()-t0)
            self.turnCount += 1
        return False
    
    def buildPath(self) :
        """ endOfPath : (int,int)
            returns : [(int,int)] (path between 'start' and 'goal')
        """
        if self.pathEnd == None :
            return None
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
        """ cell : Cell
        """
        t0 = timeit.default_timer()
        self.statusMat[x][y] = 0
        item = (self.fScoreMat[x][y], self.cellCount, x, y)
        heapq.heappush(self.openSet, item)
        self.cellCount += 1
        t1 = timeit.default_timer()
        #print "from astar:addToOPenSet : " + str(1000*(t1-t0))
    
    def lowestCell(self) :
        """ yields : Cell
            pop cells from openSet until finding a non-removed one
        """
        t0 = timeit.default_timer()
        while len(self.openSet) > 0 :
            a, b, x, y = heapq.heappop(self.openSet)
            if self.statusMat[x][y] == 0 and self.fScoreMat[x][y] == a :
                t1 = timeit.default_timer()
                #print "from astar:lowestCell : " + str(1000*(t1-t0))
                yield (x,y)
                t0 = timeit.default_timer()
    
    def neighbors(self, x0, y0) :
        """ cell : Cell
            yields : Cell (neighbor of 'cell' that are not IN_CLOSED_SET, nor obstacles)
        """
        for x, y in [(x0,y0+1), (x0,y0-1), (x0+1,y0), (x0-1,y0)] :
            t0 = timeit.default_timer()
            if self.blockMat[x][y] and self.statusMat[x][y] >= 0 :
                #t1 = timeit.default_timer()
                #print "from astar:neigbors : " + str(1000*(t1-t0))
                yield (x,y)
    
    def heuristicEstimate(self, cell) :
        """ cell : Cell
        """
        return 1.5 * util.dist(cell, self.goal)
    
    def isGoal(self, cell) :
        return util.dist(cell, self.goal) <= self.goalRadius

