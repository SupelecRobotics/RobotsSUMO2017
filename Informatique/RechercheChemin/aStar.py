# -*- coding: utf-8 -*-
"""
Created on Sat Oct 11 18:16:57 2014

@author: antoinemarechal
"""

import math

class AStar :
    """Implements the A* algorithm on an unweighted map with obstacles.
    Throughout this classes, "nodes" will be tuples (int, int).
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
        
        self._straightDist = 10     # constants
        self._diagonalDist = 14
    # end of __init__ method
    
    def aStar(self, start, goal) :
        """start : (int,int), goal : (int,int)
        Returns True if successful, False if not.
        """
        # 'start' should be the DESTINATION and 'goal' should be the CURRENT POSITION to avoid suboptimal path
        self._openSet = set([start])
        self._closedSet = set()
        self._gScore = {}
        self._fScore = {}
        self._cameFrom = {}
        
        self._gScore[start] = 0
        self._fScore[start] = self.heuristicEstimate(start, goal)
        self._cameFrom[start] = start
        
        while len(self._openSet) != 0 :         # if openSet is empty then there is no path
            
            current = self.getLowestNode()
            if current == goal :
                return True                     # if the goal is reached then the algorithm ends
            
            self._openSet.remove(current)
            self._closedSet.add(current)        # 'current' is moved to closedSet
            
            for neighbor in self.neighborNodes(current) :
                if neighbor in self._closedSet :
                    continue                    # nodes already explored cannot be improved
                newGScore = self.getGScore(neighbor, current)
                
                    # if the neighbor node is unexplored or if the cost to reach it is lowered
                if neighbor not in self._openSet or newGScore < self._gScore[neighbor] :
                    self._gScore[neighbor] = newGScore
                    self._fScore[neighbor] = newGScore + self.heuristicEstimate(neighbor, goal)
                    self._cameFrom[neighbor] = current
                    if neighbor not in self._openSet :
                        self._openSet.add(neighbor)
        return False
    # end of aStar method
    
    def constructPath(self, start, goal) :
        """start : (int,int), goal : (int,int)
        Runs aStar, then returns a list of nodes that makes up the path between 'start' and 'goal'.
        If unsuccessful, returns None.
        """
        if self.aStar(start, goal) :
            del self._cameFrom[start]   # we remove the auto-reference of start so that the following loop can end
            path = [goal]
            node = goal
            while node in self._cameFrom :
                node = self._cameFrom[node]
                path.insert(0, node)
            return path
        else :
            return None
    # end of constructPath method
    
    def neighborNodes(self, node) :
        """node : (int, int)
        Generator, iterates the free neighbors of 'node'.
        Yields neighbor nodes.
        """
        x, y = node
        nodeList = [
            (x+1, y),
            (x-1, y),
            (x, y+1),
            (x, y-1) ]
        for u,v in nodeList :
            if self._matrix[u][v] != 0 :  # if we are on a block we do nothing
                yield (u,v)
    # end of neighborNodes method
    
    def getGScore(self, newNode, baseNode) :
        """node, prevNode : (int, int)
        baseNode must be the node newNode was discovered from.
        Determines whether the best path to newNode bypasses baseNode in diagonal and returns the suitable path length
        """
        prevNode = self._cameFrom[baseNode]
        newX, newY = newNode
        prevX, prevY = prevNode
        distX = math.fabs(newX - prevX)
        distY = math.fabs(newY - prevY)
        if distX == 1 and distY == 1 :   # the best path goes diagonally from prevNode to newNode and bypasses baseNode
            return self._gScore[prevNode] + self._diagonalDist
        else :
            return self._gScore[baseNode] + self._straightDist
    # end of getGScore method
    
    def getLowestNode(self) :
        """Returns the node in openSet with the lowest fScore."""
        lowestScore = float("inf")
        lowestNode = None
        for node in self._openSet :
            if self._fScore[node] < lowestScore :
                lowestNode = node
                lowestScore = self._fScore[node]
        return lowestNode
    # end of lowestInSet method
    
    def heuristicEstimate(self, node1, node2) :
        """node1, node2 : (int, int)
        Uses Euclid distances
        """
        x1, y1 = node1
        x2, y2 = node2
        distX = x1 - x2
        distY = y1 - y2
        return math.sqrt(distX*distX + distY*distY)
    # end of heuristicEstimate method
    
    
# end of AStar class

