# -*- coding: utf-8 -*-
"""
Created on Sat Oct 18 11:08:08 2014

@author: antoinemarechal
"""

class Path :
    """Implements a path as a list of 2D coordinates, with methods to improve the path.
    """
    
    def __init__(self, path) :
        """path : list[(int,int)]
        """
        self.path = path
    # end of __init__ method
    
    def findShortcut(self, matrix) :
        """matrix : list[list[int]]
        Selects nodes in the path to form longer segments without crossing obstacles.
        """
        startNode = self.path[0]
        prevNode = startNode
        newPath = [startNode]       # the new path has the same beginning as the old one
        
        for currNode in self.path :
            if not self._isClear(startNode, currNode, matrix) :     # we check the rectangular area between startNode and currNode for obstacles
            # when an obstacle is met, the path between startNode and prevNode is clear
                if prevNode != self.path[0] :   # under some circumstances, the first node could be duplicated
                    newPath.append(prevNode)
                startNode = prevNode            # the process is repeated, starting from the latest node in the new path
            # end if
            prevNode = currNode             # prevNode is always one step behind currNode
        # end for
        newPath.append(currNode)    # the new path has the same end as the old one
        return newPath
    # end of findShortcut method
        
        
        pathIter = iter(self._path)
        startNode = next(pathIter)
        currentNode = next(pathIter)
        lastNode = None
        for lastNode in self._path :
            pass                        # lastNode is now the last item of _path
        
        while currentNode != lastNode :
            nextNode = next(pathIter)
            if self._isClear(startNode, nextNode, matrix) :
                self._path.remove(currentNode)              # if the area between startNode and nextNode is clear, then currentNode can be bypassed
            else :
                startNode = currentNode                     # if an obstacle is met, we restart from the curent node
            # end if
            currentNode = nextNode      # then we iterate
        # end while
    # end of shortcut method
            
    def _isClear(self, nodeA, nodeB, matrix) :
        """nodeA, nodeB : (int,int), matrix : list[list[int]]
        Verifies the rectangle between nodeA and nodeB is free of obstacle
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
        