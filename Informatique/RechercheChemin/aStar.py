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
    INIT, IN_OPEN_SET, IN_CLOSED_SET, REMOVED = xrange(4)    # constants
    
    def __init__(self, x, y) :
        """ x, y : int, isFree : bool
        """
        self.state = Cell.INIT
        self.x = x
        self.y = y
        self.gScore = float('inf')
        self.fScore = float('inf')
        self.origin = None
        self.id = Cell.count    # constant
        Cell.count += 1
    
    def __lt__(self, other) :
        """ other : Cell
            returns : bool (compares fScore, then gScore (inverse), then id)
            implemented for use in a HeapQueue
        """
        if self.fScore == other.fScore :
            if self.gScore == other.gScore :
                return self.id < other.id
            else :
                return self.gScore > other.gScore
        else :
            return self.fScore < other.fScore
    
    def copy(self) :
        """ returns : Cell (with identical attributes, except id)
        """
        new = Cell(self.x, self.y)
        new.state = self.state
        new.gScore = self.gScore
        new.fScore = self.fScore
        new.origin = self.origin
        return new
    
    def dist(self, x, y) :
        """ x, y : float
            returns : float (euclid distance between self and (x,y))
        """
        dX = float(self.x - x)
        dY = float(self.y - y)
        return math.sqrt(dX*dX + dY*dY)
    
    def neighbors(self) :
        """ yields : (int,int) (coordinates of side-adjacent cells)
        """
        yield (self.x, self.y + 1)
        yield (self.x, self.y - 1)
        yield (self.x + 1, self.y)
        yield (self.x - 1, self.y)
    
    def lineCoords(self, x, y, threshold) :
        """ x, y : int, threshold : float
            yields : (int,int) (coordinates of cells close to the line between self and (x,y))
        """
        fX = 1 if self.x <= x else -1   # used to fall back to a situation where
        fY = 1 if self.y <= y else -1   # self.x < x and self.y < y
        dX = fX*(x - self.x)
        dY = fY*(y - self.y)
        if dX == 0 :
            for v in xrange(dY+1) :
                yield self.x, self.y + fY*v
        elif dY == 0 :
            for u in xrange(dX+1) :
                yield self.x + fX*u, self.y
        else :
            a = float(dY)/float(dX)
            b = threshold * math.sqrt(1 + a*a)
            for u in xrange(dX+1) :
                vMin = int(max(0, math.ceil(a*u-b)))
                vMax = int(min(dY, math.floor(a*u+b)))
                for v in xrange(vMin, vMax+1):
                    yield self.x + fX*u, self.y + fY*v
    

class AStar :
    """ Implements the A* algorithm on an unweighed 2D grid with obstacles
    """
    
    def __init__(self, start, goal, matrix, threshold) :
        """ start : (float,float), goal : (int,int), matrix : [[int]], threshold : int >0
            'matrix' represents the grid : -threshold to 0 is an obstacle, anything else is a free cell
            the grid must be bordered with 0s
        """
        # for testing :
        self.turnCount = 0
        self.cellCount = 0
        
        self.start = start
        self.goal = goal
        self.pathEnd = None
        self.blockMat = [ [ (0 if matrix[x][y] <= 0 and matrix[x][y] >= -threshold else 1) for y in xrange(len(matrix[x])) ] for x in xrange(len(matrix)) ]
        self.cellMat = [ [ None for y in xrange(len(matrix[x])) ] for x in xrange(len(matrix)) ]
        self.openSet = []
        for x in xrange(int(math.floor(self.start[0])), 1+int(math.ceil(self.start[0]))) :
            for y in xrange(int(math.floor(self.start[1])), 1+int(math.ceil(self.start[1]))) :
                startCell = Cell(x, y)
                gScore = startCell.dist(self.start[0], self.start[1])
                startCell.gScore = gScore
                startCell.fScore = gScore + startCell.dist(self.goal[0], self.goal[1])
                self.addToOpenSet(startCell)
    
    def aStar(self) :
        """ runs the A* algorithm
            returns : bool (success)
        """
        for current in self.lowestCell() :
            if self.isGoal(current) :    # the algorithm ends if 'goal' is reached
                self.pathEnd = current.x, current.y
                return True
            current.state = Cell.IN_CLOSED_SET
            for neighbor in self.neighbors(current) :
                newGScore = self.getGScore(neighbor, current)
                if neighbor.state == Cell.INIT or neighbor.gScore > newGScore :
                    neighbor.gScore = newGScore
                    neighbor.fScore = newGScore + self.heuristicEstimate(neighbor)
                    neighbor.origin = current
                    self.addToOpenSet(neighbor)
            self.turnCount += 1
        return False
    
    def buildPath(self) :
        """ endOfPath : (int,int)
            returns : [(int,int)] (path between 'start' and 'goal', using shortcuts)
        """
        if self.pathEnd == None :
            return None
        else :
            
            return path
    
    def buildCompletePath(self) :
        """ endOfPath : (int,int)
            returns : [(int,int)] (path between 'start' and 'goal')
        """
        if self.pathEnd == None :
            return None
        else :
            path = [self.start, self.goal]
            current = self.cellMat[self.pathEnd[0]][self.pathEnd[1]]
            while current.origin != None :
                current = current.origin
                coord = (current.x, current.y)
                path.insert(1,coord)
            return path
    
    def addToOpenSet(self, cell) :
        """ cell : Cell
        """
        if cell.state == Cell.IN_OPEN_SET :
            self.cellMat[cell.x][cell.y].state = Cell.REMOVED
        else :
            cell.state = Cell.IN_OPEN_SET
        self.cellMat[cell.x][cell.y] = cell
        heapq.heappush(self.openSet, cell)
        self.cellCount += 1
    
    def lowestCell(self) :
        """ yields : Cell
            pop cells from openSet until finding a non-removed one
        """
        while len(self.openSet) > 0 :
            cell = heapq.heappop(self.openSet)
            if cell.state == Cell.IN_OPEN_SET :
                yield cell
    
    def neighbors(self, cell) :
        """ cell : Cell
            yields : Cell (neighbor of 'cell' that are not IN_CLOSED_SET, nor obstacles)
        """
        for x,y in cell.neighbors() :
            cell = self.cellMat[x][y]
            if cell == None : 
                if self.blockMat[x][y] != 0 :
                    yield Cell(x,y)
                else :
                    pass
            elif cell.state == Cell.IN_OPEN_SET :
                yield cell.copy()
            else :
                pass
    
    def isLineClear(self, cellA, cellB) :
        """ cellA, cellB : Cell
            returns : bool (whether the straight path between 'cellA' and 'cellB' is free of obstacles)
        """
        for x,y in cellA.lineCoords(cellB.x, cellB.y, 1) :
            if self.blockMat[x][y] == 0 :
                return False
        return True
    
    def getGScore(self, cell, origin) :
        """ cell, origin : Cell
        """
        steps = 4
        newGScore = 0
        i = origin
        while i != None and steps > 0 :
            newGScore = i.gScore + i.dist(cell.x, cell.y)
            i = i.origin
            steps -= 1
        return newGScore
    
    def heuristicEstimate(self, cell) :
        """ cell : Cell
        """
        return cell.dist(self.goal[0], self.goal[1])
    
    def isGoal(self, cell) :
        xRange = xrange(int(self.goal[0]), int(1+math.ceil(self.goal[0])))
        yRange = xrange(int(self.goal[1]), int(1+math.ceil(self.goal[1])))
        if cell.x in xRange and cell.y in yRange :
            return True
        else :
            return False










