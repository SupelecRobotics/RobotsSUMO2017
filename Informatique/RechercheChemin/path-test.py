# -*- coding: utf-8 -*-
"""
Created on Mon Oct 20 21:19:10 2014

@author: antoinemarechal
"""

import aStar
import aStarOld
import pathManager
import timeit

"""
matrix = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 2, 2, 2, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 2, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 2, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0],
    [0, 1, 1, 2, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0],
    [0, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0],
    [0,-5,-5,-5,-5,-5,-5, 0, 0, 0, 0, 0, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
"""
side = 62
matrix = [[True for x in xrange(side) ] for y in xrange(side) ]
for i in xrange(side) :
    matrix[0][i] = False
    matrix[side-1][i] = False
    matrix[i][0] = False
    matrix[i][side-1] = False

start = (1,1)
goal = (60,40,0)

t0 = timeit.default_timer()
a = aStar.AStar(start, goal, matrix)
t1 = timeit.default_timer()
print 1000 * (t1-t0)

t0 = timeit.default_timer()
print a.aStar()
t1 = timeit.default_timer()
print 1000 * (t1-t0)

t0 = timeit.default_timer()
p = a.buildPath()
t1 = timeit.default_timer()
print 1000 * (t1-t0)
