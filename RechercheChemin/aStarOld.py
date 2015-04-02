# -*- coding: utf-8 -*-
"""
Created on Mon Dec  8 21:56:35 2014

@author: antoinemarechal
"""


import math
#import heapq

def euclidDistance(cellA, cellB) :
    """ cellA, cellB : (int,int)
        returns double
    """
    distX = cellA[0] - cellB[0]
    distY = cellA[1] - cellB[1]
    return math.sqrt(distX*distX + distY*distY)
# end of euclidDistance function

def distFromLine(cell, cellA, cellB) :
    """ cell, cellA, cellB : (int,int)
        returns double
        returns the orthogonal distance (squared) between "cell" and the segment [cellA,cellB]
    """
    dx1 = float(cell[0] - cellA[0])     #
    dy1 = float(cell[1] - cellA[1])     #
    dx2 = float(cellB[0] - cellA[0])    #
    dy2 = float(cellB[1] - cellA[1])    # coordinates from cellA
    if dx2 == 0 and dy2 == 0 :
        return dx1*dx1 + dy1*dy1        # if cellA and cellB are joined : Euclid distance to cell
    else :
        num = dx1*dy2 - dx2*dy1
        den = dx2*dx2 + dy2*dy2
        return num*num/den              # else : formula found with vector calculus
# end of distFromLine function

class AStar :
    """Implements the A* algorithm on an unweighed, 2D matrix with obstacles.
    """
    
    def __init__(self, start, goal, matrix) :
        """ start, goal : (int,int)
            matrix : list[list[int]]
            matrix represents the map : 0 is an obstacle, any other (positive) value is a free cell
            matrix must be bordered with 0s
        """
        self.start = start
        self.goal = goal
        self.matrix = matrix
        self.hqCount = 0        # number of elements added to openSet (used for prioritization purpose) 
        self.openSet = set([self.start])
        self.gScore = {}
        self.fScore = {}
        self.cameFrom = {}
        
        for x in xrange(0,len(self.matrix)-1) :
            for y in xrange(0,len(self.matrix[x])-1) :
                if self.matrix[x][y] != 0 :
                    self.matrix[x][y] = 1   # normalize the matrix : blocks are 0, everything else is 1
        self.gScore[self.start] = 0
        self.fScore[self.start] = euclidDistance(self.start, self.goal)
    # end of __init__ method
    
    def aStar(self) :
        """ runs the A* algorithm.
            returns True if successful, False if not.
        """
        while len(self.openSet) != 0 :
            current = self.lowestCell()
            if current == self.goal :
                return True
            self.addToClosedSet(current)
            for neighbor in self.neighborCells(current) :
                newGScore = self.gScore[current] + 1
                if neighbor not in self.openSet or self.gScore[neighbor] > newGScore :
                    self.gScore[neighbor] = newGScore
                    self.fScore[neighbor] = newGScore + euclidDistance(neighbor, self.goal)
                    self.cameFrom[neighbor] = current
                    if neighbor not in self.openSet :
                        self.openSet.add(neighbor)
        return False
    # end of aStar method
    
    def buildPath(self) :
        """ returns list[(int,int)] 
            reconstitutes the path between start and goal
        """
        if self.goal not in self.cameFrom :
            return None
        else :
            """
            path = [self.goal]
            target = self.goal
            while target != self.start :
                predecessor = target
                i = target
                while i != self.start :
                    i = self.cameFrom[i]
                    if self.isLineClear(i,target) :
                        predecessor = i
                path.insert(0, predecessor)
                target = predecessor
            """
            path = [self.start]
            current = self.start
            while current != self.goal :
                i = self.goal
                while not self.isLineClear(i, current) :
                    i = self.cameFrom[i]
                current = i
                path.append(current)
            ""
            return path
    # end of buildPath method
    
    def buildCompletePath(self) :
        """ for testing purposes
        """
        if self.goal not in self.cameFrom :
            return None
        else :
            path = [self.goal]
            cell = self.goal
            while cell in self.cameFrom :
                cell = self.cameFrom[cell]
                path.insert(0, cell)
            return path
    # end of buildPath method
    
    def addToClosedSet(self, cell) :
        """ cell : (int,int)
            sets the element of "matrix" associated to "cell" to -1
        """
        self.matrix[cell[0]][cell[1]] = -1
    # end of addToClosedSet method
    
    def addToOpenSet(self, cell) :
        """ cell : (int,int)
            adds "cell" to the Heap Queue "openSet" with fScore as primary priority and hqCount as secondary priority
        """
        
    # end of addToOpenSet method
    
    def lowestCell(self):
        """ returns (int,int)
            removes the lowest priority element from "openSet" and returns the associated cell
        """
        lScore = float("inf")
        lCell = None
        for cell in self.openSet :
            if self.fScore[cell] < lScore :
                lCell = cell
                lScore = self.fScore[cell]
        self.openSet.remove(lCell)
        return lCell
    # end of lowestCell method
    
    def neighborCells(self, cell) :
        """ cell : (int,int)
            yields (int,int)
            finds the cells adjacent to "cell" that can be explored
        """
        cellList = [
            (cell[0]+1, cell[1]),
            (cell[0]-1, cell[1]),
            (cell[0], cell[1]+1),
            (cell[0], cell[1]-1) ]
        for x,y in cellList :
            if self.matrix[x][y] <= 0 :     # obstacles cannot be explored
                pass
            else :
                yield (x,y)
    # end of neighborCells method
    
    def isLineClear(self, cellA, cellB) :
        """ cellA, cellB : (int,int)
            returns boolean
            verifies whether the area around the straight line between "cellA" and "cellB" is free of obstacles
        """
        threshold = .6      # constant : determines the width of the area
        xMin = min(cellA[0], cellB[0])
        xMax = max(cellA[0], cellB[0])
        yMin = min(cellA[1], cellB[1])
        yMax = max(cellA[1], cellB[1])
        for x in xrange(xMin, xMax+1) :
            for y in xrange(yMin, yMax+1) :
                if distFromLine((x,y), cellA, cellB) > threshold :
                    pass
                elif self.matrix[x][y] == 0 :
                    return False            # the area contains an obstacle
        return True
    # end of isLineClear
    
# end of AStar class