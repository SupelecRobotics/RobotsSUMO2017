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
        new = Cell(self.x, self.y, True)
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
    
    def __init__(self, start, goal, matrix) :
        """ start, goal : (int,int), matrix : [[int]]
            'matrix' represents the grid : 0 is an obstacle, anything else is a free cell
            the grid must be bordered with 0s
        """
        self.start = start
        self.goal = goal
        self.matrix = [ [ Cell(x, y, matrix[x][y] != 0) for y in xrange(len(matrix[x])) ] for x in xrange(len(matrix)) ]
        self.openSet = []
        startCell = self.matrix[self.start[0]][self.start[1]]
        startCell.gScore = 0
        startCell.fScore = startCell.dist(self.goal[0], self.goal[1])
        self.addToOpenSet(startCell)
    
    def aStar(self) :
        """ runs the A* algorithm
            returns : bool (success)
        """
        for current in self.lowestCell() :
            if (current.x, current.y) == self.goal :    # the algorithm ends if 'goal' is reached
                return True
            current.state = Cell.IN_CLOSED_SET
            newGScore = current.gScore + 1
            for neighbor in self.neighbors(current) :
                if neighbor.state == Cell.VOID or neighbor.gScore > newGScore :
                    neighbor.gScore = newGScore
                    neighbor.fScore = newGScore + neighbor.dist(self.goal[0], self.goal[1])
                    neighbor.origin = current
                    self.addToOpenSet(neighbor)
    
    def buildPath(self) :
        """ returns : [(int,int)] (path between 'start' and 'goal', using shortcuts)
        """
        if self.matrix[self.goal[0]][self.goal[1]].state == Cell.VOID :
            return None
        else :
            path = [self.start]
            current = self.matrix[self.start[0]][self.start[1]]
            while (current.x, current.y) != self.goal :
                i = self.matrix[self.goal[0]][self.goal[1]]
                while not self.isLineClear(current, i):
                    i = i.origin
                current = i
                coord = (current.x, current.y)
                path.append(coord)
            return path
    
    def buildCompletePath(self) :
        """ for testing purposes
        """
        path = [self.goal]
        current = self.matrix[self.goal[0]][self.goal[1]]
        while (current.x, current.y) != self.start :
            current = current.origin
            coord = (current.x, current.y)
            path.insert(0,coord)
        return path
    
    def addToOpenSet(self, cell) :
        """ cell : Cell
        """
        if cell.state == Cell.IN_OPEN_SET :
            self.matrix[cell.x][cell.y].state = Cell.REMOVED
            self.matrix[cell.x][cell.y] = cell
        else :
            cell.state = Cell.IN_OPEN_SET
        heapq.heappush(self.openSet, cell)
    
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
            yields : Cell (neighbor of 'cell' that are not BLOCK or IN_CLOSED_SET)
            creates a new Cell if current one is IN_OPEN_SET
        """
        for x,y in cell.neighbors() :
            cell = self.matrix[x][y]
            if cell.state == Cell.VOID :
                yield cell
            elif cell.state == Cell.IN_OPEN_SET :
                yield cell.copy()
            else :
                pass
    
    def isLineClear(self, cellA, cellB) :
        """ cellA, cellB : Cell
            returns : bool (whether the straight path between 'cellA' and 'cellB' is free of obstacles)
        """
        for x,y in cellA.lineCoords(cellB.x, cellB.y, 1) :
            if self.matrix[x][y].state == Cell.BLOCK :
                return False
        return True
    
    










