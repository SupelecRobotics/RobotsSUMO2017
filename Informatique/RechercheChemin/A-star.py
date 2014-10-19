# -*- coding: utf-8 -*-
"""
Created on Sat Oct 11 18:16:57 2014

@author: antoinemarechal
"""

import math

class AStar :
    """Implements the A* algorithm on an unweighted map with obstacles.
    """
    
    def __init__(self, matrix) :
        """matrix : list[list[int]]
        For each element of 'matrix' : 0 is a block, any other number is a free square (1 should be used for clarity).
        The matrix is not necessarily rectangular.
        The matrix MUST be bordered with 0s (blocks) to prevent the algorithm from trying to exit it.
        """
        self._matrix = matrix
        
        self._openSet = None        # set : nodes currently being explored
        self._closedSet = None      # set : nodes already explored 
        self._gScore = None         # dict : cost from start to node along best known path
        self._fScore = None         # dict : estimated cost from start to goal through node
        self._cameFrom = None       # dict : predecessor of node in best known path from start
        
        self._SQRT2 = math.sqrt(2)  # constant
    # end of __init__ method
    
    def aStar(self, start, goal) :
        """start : (int,int), goal : (int,int)
        Returns True if successful, False if not.
        """
        self._openSet = set([start])
        self._closedSet = set()
        self._gScore = {}
        self._fScore = {}
        self._cameFrom = {}
        
        self._gScore[start] = 0
        self._fScore[start] = self.heuristicEstimate(start, goal)
        
        while len(self._openSet) != 0 :         # if openSet is empty then there is no path
            
            current = self.getLowestNode()
            if current == goal :
                return True                     # if the goal is reached then the algorithm ends
            
            self._openSet.remove(current)
            self._closedSet.add(current)        # 'current' is moved to closedSet
            
            for neighbor, dist in self.neighborNodes(current) :
                if neighbor in self._closedSet :
                    continue                    # nodes already explored cannot be improved
                # end if
                newGScore = self._gScore[current] + dist    # cost from start to 'neighbor' through 'current'
                    # if the neighbor node is unexplored or if the cost to reach it is lowered
                if neighbor not in self._openSet or newGScore < self._gScore[neighbor] :
                    self._gScore[neighbor] = newGScore
                    self._fScore[neighbor] = newGScore + self.heuristicEstimate(neighbor, goal)
                    self._cameFrom[neighbor] = current
                    if neighbor not in self._closedSet :
                        self._openSet.add(neighbor)
                    # end if
                #end if
            # end for
        # end while
        return False
    # end of aStar method
    
    def constructPath(self, start, goal) :
        """start : (int,int), goal : (int,int)
        Runs aStar, then returns a list of nodes that makes up the path between 'start' and 'goal'.
        If unsuccessful, returns None.
        """
        if self.aStar(start, goal) :
            path = [goal]
            node = goal
            while node in self._cameFrom :
                node = self._cameFrom[node]
                path.insert(0, node)
            # end while
            return path
        else :
            return None
        # end if
    # end of constructPath method
    
    def neighborNodes(self, node) :
        """node : (int, int)
        Generator, iterates the free neighbors of 'node'.
        Yields a tuple : neighbor(int,int), distance(float).
        """
        # TO DO : the diagonal movements could be ignored (when used with Path.findShortcut)
        xNode, yNode = node
        for i in xrange(-1, 2) :
            for j in xrange(-1, 2) :
                x = xNode + i
                y = yNode + j
                if i == 0 and j == 0 :          # if we are on the node we do nothing
                    continue
                elif self._matrix[x][y] == 0 :  # if we are on a block we do nothing
                    continue
                else :
                    if i*j == 0 :
                        yield ((x, y), 1)               # along a horizontal or vertical the distance is 1
                    else :
                        yield ((x, y), self._SQRT2)     # along a diagonal the distance is sqrt(2)
                    # end if
                # end if
            # end for
        # end for
    # end of neighborNodes method
    
    def getLowestNode(self) :
        """Returns the element of openSet with the lowest fScore."""
        lowestScore = float("inf")
        lowestNode = None
        for node in self._openSet :
            if self._fScore[node] < lowestScore :
                lowestNode = node
                lowestScore = self._fScore[node]
            # end if
        # end for
        return lowestNode
    # end of lowestInSet method
    
    def heuristicEstimate(self, node1, node2) :
        """node : (int, int)
        Travel is along horizontals, verticals and 45° diagonals.
        """
        x1, y1 = node1
        x2, y2 = node2
        xDist = math.fabs(x1 - x2)
        yDist = math.fabs(y1 - y2)
        if xDist < yDist :
            return xDist * (self._SQRT2 - 1) + yDist
        else :
            return xDist + yDist * (self._SQRT2 - 1)
        # end if
    # end of heuristicEstimate method
    
    
# end of AStar class


# template 14x8 (plus borders) matrix :

#matrix = [
#[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#[0,2,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
#[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
#[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
#[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
#[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
#[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
#[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
#[0,1,1,1,1,1,1,1,1,1,1,1,1,1,2,0],
#[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]






