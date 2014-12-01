# -*- coding: utf-8 -*-
"""
Created on Sat Oct 18 11:08:08 2014

@author: antoinemarechal
"""

import math

class Path :
    """Implements a path as a list of 2D coordinates, with methods to improve the path.
    """
    
    def __init__(self, path) :
        """path : list[(int,int)]
        The path must not cross itself (all nodes must be differents) or the improvement method might removes the wrong nodes
        """
        self.path = path
    # end of __init__ method
    
    def findShortcut(self, matrix) :
        """matrix : list[list[int]]
        Selects nodes in the path to form longer segments without crossing obstacles.
        Several passes are necessary to find the best path.
        """
        prevLen = len(self.path) + 1
            # the algorithm stops when there is one segment left,
            # or when it can't shorten the path more
        while len(self.path) > 2 and len(self.path) < prevLen :
            prevLen = len(self.path)
            
            startNode = self.path[0]
            prevNode = startNode
            newPath = [startNode]               # the new path has the same beginning as the old one
            
            for currNode in self.path[1:] :
                if not Path._isClear(startNode, currNode, matrix) :     # we check the rectangular area between startNode and currNode for obstacles
                    newPath.append(prevNode)    # when an obstacle is met, the path between startNode and prevNode is clear
                    startNode = prevNode        # the process is repeated, starting from the latest node in the new path
                prevNode = currNode             # prevNode is always one step behind currNode
            newPath.append(currNode)            # the new path has the same end as the old one
            self.path = newPath
    # end of findShortcut method
    
    def clearPath(self) :
        """Merges aligned segments in the path
        """
        if len(self.path) <= 2 :
            return                          # if there is one segment or less, there is nothing to do
        node1 = self.path[0]
        node2 = self.path[1]
        for node3 in self.path[2:] :        # node1, node2, node3 are three consecutive nodes along the path
            if Path._isAligned(node1, node2, node3) :
                self.path.remove(node2)     # if three consecutive nodes are aligned, the median one is superfluous
                node2 = node3               # only node2 is incremented ; node1 is unchanged
            else :
                node1 = node2               # both nodes are incremented
                node2 = node3
    # end of clearPath method
    
    @staticmethod
    def _isClear(nodeA, nodeB, matrix) :
        """nodeA, nodeB : (int,int), matrix : list[list[int]]
        Verifies whether the straight line between nodeA and nodeB is free of obstacle
        """
        threshold = .5  # how close to the line the cells must be to be checked
        xA, yA = nodeA
        xB, yB = nodeB
        xMin = min(xA, xB)
        xMax = max(xA, xB)
        yMin = min(yA, yB)
        yMax = max(yA, yB)
        for x in xrange(xMin, xMax+1) :
            for y in xrange(yMin, yMax+1) :
                if Path._distFromLine((x,y), nodeA, nodeB) > threshold :
                    pass
                elif matrix[x][y] == 0 :
                    return False            # the rectangle contains an obstacle
        return True
    # end of _isClear method
    
    @staticmethod
    def _distFromLine(node, nodeA, nodeB) :
        """node1, node2, node3 : (int,int)
        Calculates the square of the orthogonal distance between node and the segment [nodeA,nodeB]
        """
        x, y = node
        xA, yA = nodeA
        xB, yB = nodeB
        dx1 = float(x-xA)   #
        dy1 = float(y-yA)   #
        dx2 = float(xB-xA)  #
        dy2 = float(yB-yA)  # coordinates from nodeA
        if dx2 == 0 and dy2 == 0 :
            return dx1*dx1 + dy1*dy1    # if nodeA and nodeB are joined : Euclid distance to node
        else :
            num = dx1*dy2 - dx2*dy1
            den = dx2*dx2 + dy2*dy2
            return num*num/den          # else : formula found with vector calculus
    # end of _distFromLine method
    
    @staticmethod
    def _isAligned(node1, node2, node3) :
        """node1, node2, node3 : (int,int)
        Verifies whether all three nodes are aligned
        """
        x1, y1 = node1
        x2, y2 = node2
        x3, y3 = node3
        dX12 = math.fabs(x1 - x2)
        dX23 = math.fabs(x2 - x3)
        dY12 = math.fabs(y1 - y2)
        dY23 = math.fabs(y2 - y3)
        return (dX12 * dY23) == (dX23 * dY12)   # use cross-product to verify alignment
    
    
# end of Path class
        