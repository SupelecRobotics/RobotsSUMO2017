# -*- coding: utf-8 -*-
"""
Created on Mon Oct 20 21:19:10 2014

@author: antoinemarechal
"""

import aStar
import pathTools

matrix = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,2,2,2,0,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,2,0,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,2,0,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,2,0,1,1,1,1,1,1,0,1,1,1,0],
    [0,1,1,2,2,2,2,1,1,1,1,0,1,1,1,0],
    [0,1,1,1,1,1,2,1,1,1,1,0,1,1,1,0],
    [0,1,1,1,1,1,2,0,0,0,0,0,1,1,1,0],
    [0,1,1,1,1,1,2,2,2,2,2,2,2,2,2,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

start = (3,1)
goal = (8,14)

a = aStar.AStar(matrix)

path = a.constructPath(start, goal)

print path

p = pathTools.Path(path)

p.findShortcut(matrix)

print p.path

p.clearPath()

print p.path