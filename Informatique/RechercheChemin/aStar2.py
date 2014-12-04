# -*- coding: utf-8 -*-
"""
Created on Thu Dec  4 22:07:19 2014

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
        self.matrix = matrix
        self.start = start
        self.goal = goal
        self.openSet = set([start]) # newly discovered nodes
        self.closedSet = set([])    # already explored nodes
        self.gScore = {}            # distance from any node to start, along the simplified path
        self.fScore = {}            # sum of gScore and heuristic estimate
        self.directPre = {}         # predecessor of each node in the complete path
        self.bestPre = {}           # predecessor of each node in the simplified path
        self.gScore[self.start] = 0
        self.fScore[self.start] = self.heuristicEstimate(self.start)
    # end of __init__ method
    
    def aStar(self) :
        """ runs the A* algorithm.
            returns True if successful, False if not.
        """
        while len(self.openSet) != 0 :      # if openSet becomes empty then there is no path
            current = self.lowestNode()
            if current == self.goal :
                return True                 # if the goal is reached then the algorithm ends
            self.openSet.remove(current)
            self.closedSet.add(current)     # 'current' is moved to closedSet
            for neighbor in self.neighborNodes(current) :
                predecessor = self.predecessorNode(neighbor, current)
                newGScore = self.gScore[predecessor] + AStar.euclidDistance(neighbor, predecessor)
                if neighbor not in self.openSet or self.gScore[neighbor] > newGScore :
                                            # neighbor is discovered for the first time, or a better path has been found
                    self.gScore[neighbor] = newGScore
                    self.fScore[neighbor] = newGScore + self.heuristicEstimate(neighbor)
                    self.directPre[neighbor] = current
                    self.bestPre[neighbor] = predecessor
                    if neighbor not in self.openSet :
                        self.openSet.add(neighbor)
        return False
    # end of aStar method
    
    def buildPath(self) :
        """ returns list[(int,int)] 
            reconstitutes the path between start and goal
        """
        if self.goal not in self.bestPre :
            return None
        else :
            path = [self.goal]
            node = self.goal
            while node in self.bestPre :
                node = self.bestPre[node]
                path.insert(0, node)
            return path
    # end of buildPath method
    
    def buildCompletePath(self) :
        """ for testing purposes
        """
        if self.goal not in self.directPre :
            return None
        else :
            path = [self.goal]
            node = self.goal
            while node in self.directPre :
                node = self.directPre[node]
                path.insert(0, node)
            return path
    # end of buildPath method
    
    def lowestNode(self) :
        """ returns (int,int)
            finds the node in openSet with the lowest fScore
        """
        lowestScore = float("inf")
        lowestNode = None
        for node in self.openSet :
            if self.fScore[node] < lowestScore :
                lowestNode = node
                lowestScore = self.fScore[node]
        return lowestNode
    # end of getLowestNode method
    
    def neighborNodes(self, node) :
        """ node : (int,int)
            yields (int,int)
            finds the nodes adjacent to "node" that can be explored
        """
        nodeList = [
            (node[0]+1, node[1]),
            (node[0]-1, node[1]),
            (node[0], node[1]+1),
            (node[0], node[1]-1) ]
        for x,y in nodeList :
            if self.matrix[x][y] == 0 :     # obstacles cannot be explored
                pass
            elif (x,y) in self.closedSet :  # nodes already explored cannot be improved
                pass
            else :
                yield (x,y)
    # end of neighborNodes method
    
    def predecessorNode(self, current, origin) :
        """ node, origin : (int,int)
            returns (int,int)
            finds the furthest node on the path from "origin" that can be accessed in a straight line from "current"
        """
        predecessor = origin
        node = origin
        while node in self.directPre :
            node = self.directPre[node]
            if self.isLineClear(current, node) :
                predecessor = node
        return predecessor
    # end of predecessorNode
    
    def isLineClear(self, nodeA, nodeB) :
        """ nodeA, nodeB : (int,int)
            returns boolean
            verifies whether the area around the straight line between "nodeA" and "nodeB" is free of obstacles
        """
        threshold = .6      # constant : determines the width of the area
        xMin = min(nodeA[0], nodeB[0])
        xMax = max(nodeA[0], nodeB[0])
        yMin = min(nodeA[1], nodeB[1])
        yMax = max(nodeA[1], nodeB[1])
        for x in xrange(xMin, xMax+1) :
            for y in xrange(yMin, yMax+1) :
                if AStar.distFromLine((x,y), nodeA, nodeB) > threshold :
                    pass
                elif self.matrix[x][y] == 0 :
                    return False            # the area contains an obstacle
        return True
    # end of isLineClear
    
    @staticmethod
    def distFromLine(node, nodeA, nodeB) :
        """ node, nodeA, nodeB : (int,int)
            returns double
            returns the orthogonal distance (squared) between "node" and the segment [nodeA,nodeB]
        """
        dx1 = float(node[0] - nodeA[0])     #
        dy1 = float(node[1] - nodeA[1])     #
        dx2 = float(nodeB[0] - nodeA[0])    #
        dy2 = float(nodeB[1] - nodeA[1])    # coordinates from nodeA
        if dx2 == 0 and dy2 == 0 :
            return dx1*dx1 + dy1*dy1        # if nodeA and nodeB are joined : Euclid distance to node
        else :
            num = dx1*dy2 - dx2*dy1
            den = dx2*dx2 + dy2*dy2
            return num*num/den              # else : formula found with vector calculus
    # end of distFromLine method
    
    def heuristicEstimate(self, node) :
        """ node : (int,int)
            returns (int,int)
        """
        return AStar.euclidDistance(node, self.goal)
    # end of heuristicEstimate method
    
    @staticmethod
    def euclidDistance(nodeA, nodeB) :
        """ nodeA, nodeB : (int,int)
            returns double
        """
        distX = nodeA[0] - nodeB[0]
        distY = nodeA[1] - nodeB[1]
        return math.sqrt(distX*distX + distY*distY)
    # end of euclidDistance
    
# end of AStar class