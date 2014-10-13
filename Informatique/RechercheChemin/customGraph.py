# -*- coding: utf-8 -*-
"""
Created on Wed Oct 08 22:12:10 2014

@author: Fabien
Copy of code on Amit's game programming blog
No need to take care of graph's edges thanks to neighbours function
Visibility graph needed??? latice  grids , flow fields??
    http://www.gamasutra.com/blogs/MatthewKlingensmith/20130907/199787/Overview_of_Motion_Planning.php
PRM
"""

all_nodes = []
for x in range(20):
    for y in range(10):
        all_nodes.append([x, y])

def neighbours(node):
    dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    #dirs = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [-1, 1], [-1, -1], [1, -1]]
    #if you want a eight directional moving agent 
    result = []
    for dir in dirs:
        neighbour = [node[0] + dir[0], node[1] + dir[1]]
        if neighbour in all_nodes:
            result.append(neighbour)
    return result