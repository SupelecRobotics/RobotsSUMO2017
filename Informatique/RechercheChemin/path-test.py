# -*- coding: utf-8 -*-
"""
Created on Mon Oct 20 21:19:10 2014

@author: antoinemarechal
"""

import aStar
import aStarOld
import pathManager
import time

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

threshold = 0

mat = [ [ (matrix[x][y] > 0 or matrix[x][y] < -threshold) for y in xrange(len(matrix[x])) ] for x in xrange(len(matrix)) ]

start = (1,1)
goal = (8,14)

#a = aStar.AStar(start, goal, mat)
#
#a.aStar()
#
#p = a.buildCompletePath()

t1 = time.clock()
pm = pathManager.PathManager(matrix)
pm.setThreshold(threshold)
t2 = time.clock()
pm.findPath(start, goal)
p = pm.path
t3 = time.clock()
print p
print t2 - t1
print t3 - t2

for x in xrange(len(a.cellMat)) :
    s = ""
    for y in xrange(len(a.cellMat[x])) :
        if not a.blockMat[x][y]  :
            s += "# "
        else :
            c = a.cellMat[x][y]
            if c == None :
                s += "  "
            elif (x,y) in p :
                s += "@ "
            elif c.state == aStar.Cell.IN_OPEN_SET :
                s += "o "
            elif c.state == aStar.Cell.IN_CLOSED_SET :
                s += "x "
            else :
                s += "  "
    print s



"""



side = 62
m = [[1 for x in xrange(side)] for x in xrange(side)]

for i in xrange(side) :
    m[i][0] = 0
    m[i][side-1] = 0
    m[0][i] = 0
    m[side-1][i] = 0

begin = (1,1)
end = (40,60)

#t0 = time.clock()
#a = aStar.AStar(begin, end, m)
#t1 = time.clock()
#print t1 - t0
#a.aStar()
#t2 = time.clock()
#print t2 - t1
#p = a.buildCompletePath()
#t3 = time.clock()
#print t3 - t2
#sp = aStar.PathSimplifier(m)
#print sp.simplifyPath(p)
#t4 = time.clock()
#print t4 - t3

t1 = time.clock()
pm = pathManager.PathManager(m)
pm.setThreshold(0)
t2 = time.clock()
pm.findPath(begin, end)
p = pm.path
t3 = time.clock()
print p
print t2 - t1
print t3 - t2

"""

a = aStar.AStar(f.forest)
print time.clock()
a.aStar(begin,end)
print time.clock()
p = pathTools.Path(a.constructPath(begin,end))
p.findShortcut(f.forest)
p = p.path
""
for i in xrange(0,len(p2)) :
    x, y = p2[i]
    f.forest[x][y] = 20
""
for i in xrange(0,len(p)) :
    x, y = p[i]
    m[x][y] = 10

for x in xrange(0,side) :
    str = ""
    for y in xrange(0,side) :
        n = m[x][y]
        if n == 0 :
            str += "# "
        elif n == 25 :
            str += ". "
        elif n == 10 :
            str += "@ "
        else :
            str += "  "
    print str
"""
