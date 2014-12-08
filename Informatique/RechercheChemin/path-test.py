# -*- coding: utf-8 -*-
"""
Created on Mon Oct 20 21:19:10 2014

@author: antoinemarechal
"""

import aStar
import aStar2
import aStar3
import aStar4
import pathTools
import time

"""
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
"""

""
side = 1000
m = [[1 for x in xrange(side)] for x in xrange(side)]

for i in xrange(side) :
    m[i][0] = 0
    m[i][side-1] = 0
    m[0][i] = 0
    m[side-1][i] = 0

begin = (1,1)
end = (200,300)

a = aStar3.AStar(begin, end, m)
t1 = time.clock()
a.aStar()
t2 = time.clock()
print t2 - t1
p = a.buildPath()
print time.clock() - t2
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
