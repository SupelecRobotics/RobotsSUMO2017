# -*- coding: utf-8 -*-
"""
Created on Mon Oct 20 22:50:52 2014

@author: Fabien
"""

import aStar
import pathTools

class Pathfinding():
    def __init__(self, matrix, start, goal):
        self.matrix = matrix
        self.start = start
        self.goal = goal

    def resetPath(self, start, goal): #method that changes start and goal
        self.start = start
        self.goal = goal
        # reset matrix?
    
    def findPath(self):
        a = aStar.AStar(matrix)
        self.path = a.constructPath(self.start, self.goal)
        p = pathTools.Path(self.path)
        self.path = p.path
        self.highlightPath(4)        
        
        p.findShortcut(self.matrix)
        p.clearPath()
        self.path = p.path
        self.highlightPath(5)
        
    def highlightPath(self, number):
        for coord in self.path:
            self.matrix[coord[0]][coord[1]] = number
            
    def printMatrix(self):
        for line in self.matrix:
            s = ""
            for cell in line :
                if cell == 0 :
                    s += "##"
                elif cell == 1 :
                    s += "  "
                else :
                    s += "x "
            # end for
            print s
        # end for
            


matrix = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,0,1,1,1,1,1,1,0,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0],
    [0,1,1,1,1,1,1,0,0,0,0,0,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

print (3,1)[0]    
pathF = Pathfinding(matrix, (3,1), (8,12))
pathF.findPath()
pathF.printMatrix()
