# -*- coding: utf-8 -*-
"""
Created on Mon Dec  8 21:56:35 2014

@author: antoinemarechal
"""


import math

class AStar :
    """Implements the A* algorithm on an unweighed, 2D matrix with obstacles.
    """
    
    def __init__(self, start, goal, matrix) :
        """ start, goal : (int,int)
            matrix : list[list[int]]
            matrix represents the map : 0 is an obstacle, anything else is a free square
            matrix must be bordered with 0s
        """
        
    # end of __init__ method
    
    def aStar(self) :
        """ runs the A* algorithm.
            returns True if successful, False if not.
        """
        
    # end of aStar method
    
    def buildPath(self) :
        """ returns list[(int,int)] 
            reconstitutes the path between start and goal
        """
        
    # end of buildPath method
    
    def buildCompletePath(self) :
        """ for testing purposes
        """
        
    # end of buildPath method
    
    
    def neighborCells(self, cell) :
        """ cell : (int,int)
            yields (int,int)
            finds the cells adjacent to "cell" that can be explored
        """
        
    # end of neighborCells method
    
    @staticmethod
    def euclidDistance(cellA, cellB) :
        """ cellA, cellB : (int,int)
            returns double
        """
        distX = cellA[0] - cellB[0]
        distY = cellA[1] - cellB[1]
        return math.sqrt(distX*distX + distY*distY)
    # end of euclidDistance
    
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
                if AStar.distFromLine((x,y), cellA, cellB) > threshold :
                    pass
                elif self.matrix[x][y] == 0 :
                    return False            # the area contains an obstacle
        return True
    # end of isLineClear
    
    @staticmethod
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
    # end of distFromLine method
    
# end of AStar class