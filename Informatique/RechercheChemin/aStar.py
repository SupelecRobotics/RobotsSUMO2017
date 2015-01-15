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
        self.blockMat = matrix
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
                newGScore = current.gScore + current.dist(neighbor.x, neighbor.y)
                if neighbor.state == Cell.INIT or neighbor.gScore > newGScore :
                    neighbor.gScore = newGScore
                    neighbor.fScore = newGScore + self.heuristicEstimate(neighbor)
                    neighbor.origin = current
                    self.addToOpenSet(neighbor)
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
            current = self.cellMat[self.pathEnd[0]][self.pathEnd[1]]
            while current.origin != None :
                current = current.origin
                coord = (current.x, current.y)
                path.insert(0,coord)
            if self.start != path[0] :
                path.insert(0, self.start)
            if self.goal != self.pathEnd :
                path.append(self.goal)
            return path
    
    def addToOpenSet(self, cell) :
        """ cell : Cell
        """
        if cell.state == Cell.IN_OPEN_SET : # if cell is already in openSet : mark it as 'removed' and add a copy
            cell.state = Cell.REMOVED
            cell = cell.copy()
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
            if not self.blockMat[x][y] :            # if obstacle : no neighbor
                pass
            else :
                if self.cellMat[x][y] == None :     # if void neighbor : create a new cell
                    yield Cell(x,y)
                elif self.cellMat[x][y].state == Cell.IN_OPEN_SET : # if neighbor in open set : return it
                    yield self.cellMat[x][y]
                else :                              # if neighbor in closed set : don't return it
                    pass
    
    def heuristicEstimate(self, cell) :
        """ cell : Cell
        """
        return 1.5 * cell.dist(self.goal[0], self.goal[1])
    
    def isGoal(self, cell) :
        return cell.dist(self.goal[0], self.goal[1]) <= self.goalRadius

