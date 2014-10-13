# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 19:11:58 2014

@author: Fabien
"""

graph = []

with open('le450_25a.col','r') as textfile:
    #textfile = file('hello.txt','r')
    #print textfile.readline()
    for line in textfile:
        words = line.split(" ")
        if words[0] == 'p' :
            graph = [[] for i in range(int(words[2]))]
        elif words[0] == 'e' :
            graph[int(words[1]) - 1].append(int(words[2]) - 1)
            graph[int(words[2]) - 1].append(int(words[1]) - 1)
            print words[1] + " " + words[2]
    print len(graph)

