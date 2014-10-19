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
        """
        if len(self.path) <= 2 :
            return                          # if there is one segment or less, there is nothing to do
        startNode = self.path[0]
        prevNode = startNode
        newPath = [startNode]               # the new path has the same beginning as the old one
        
        for currNode in self.path[1:] :
            if not self._isClear(startNode, currNode, matrix) :     # we check the rectangular area between startNode and currNode for obstacles
                newPath.append(prevNode)    # when an obstacle is met, the path between startNode and prevNode is clear
                startNode = prevNode        # the process is repeated, starting from the latest node in the new path
            # end if
            prevNode = currNode             # prevNode is always one step behind currNode
        # end for
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
            if self._isAligned(node1, node2, node3) :
                self.path.remove(node2)     # if three consecutive nodes are aligned, the median one is superfluous
                node2 = node3               # only node2 is incremented ; node1 is unchanged
            else :
                node1 = node2               # both nodes are incremented
                node2 = node3
            # end if
        # end for
    # end of clearPath method
    
    def _isClear(self, nodeA, nodeB, matrix) :
        """nodeA, nodeB : (int,int), matrix : list[list[int]]
        Verifies whether the rectangle between nodeA and nodeB is free of obstacle
        """
        xA, yA = nodeA
        xB, yB = nodeB
        xMin = min(xA, xB)
        xMax = max(xA, xB)
        yMin = min(yA, yB)
        yMax = max(yA, yB)
        for x in xrange(xMin, xMax+1) :
            for y in xrange(yMin, yMax+1) :
                if matrix[x][y] == 0 :
                    return False            # the rectangle contains an obstacle
                # end if
            # end for
        # end for
        return True
    # end of _isClear method
    
    def _isAligned(self, node1, node2, node3) :
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
        