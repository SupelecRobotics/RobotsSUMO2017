# -*- coding: utf-8 -*-
"""
Created on Mon Oct 20 21:19:10 2014

@author: antoinemarechal
"""

import aStar
import aStarOld
import pathManager
import timeit
import objectives
import random

""
matrix = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 2, 1, 1, 0, 8, 1, 1, 1, 1, 2, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 4, 1, 1, 0],
    [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 2, 1, 0],
    [0, 1, 1, 2, 2, 1, 2, 1, 4, 1, 1, 0, 1, 1, 8, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 8, 1, 1, 2, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

pm = objectives.PriorityManager()
pm.matrix = matrix
pm.threshold = 0
pm.position = (1,1)

objF1 = objectives.FixedObjective((1,5), 0, 0)
objF2 = objectives.FixedObjective((8,9), 0, 1)
objF3 = objectives.FixedObjective((4,14), 5, 2)

objM1 = objectives.MobileObjective((4,8), 2, 2, 3)
objM2 = objectives.MobileObjective((2,12), 1, 0, 4)

pm.add(objF1)
pm.add(objF2)
pm.add(objF3)
pm.add(objM1)
pm.add(objM2)

print pm.position
while len(pm.list) > 0 :
    obj, point = pm.getNextPoint()
    print point
    if obj.isComplete :
        print obj.script
    pm.position = point



