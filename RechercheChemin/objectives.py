# -*- coding: utf-8 -*-
"""
Created on Mon Feb 23 22:52:00 2015

@author: antoinemarechal
"""

import util
import pathManager

class Objective :
    """ Implement an objective for the robot, with location and priority
    """
    
    def __init__(self, goal, priority) :
        """ goal : (int,int), priority : int
        """
        self.goal = goal
        self.priority = priority
        self.isComplete = False
    
    def value(self, position) :
        """ position : (int,int)
            returns : int
        """
        return util.dist(self.goal[:2], position) - self.priority
    

class PriorityManager :
    """ Implements a list of 'Objective' instances
        Can add and remove objectives
        Can find the highest-priority objective
    """
    
    def __init__(self) :
        
        self.list = []
        self.matrix = None      # may be accessed directly
        self.threshold = 0      # may be accessed directly
        self.position = (0,0)   # may be accessed directly
        
    def addObjective(self, obj) :
        """ obj : Objective
            adds 'obj' to the list if it's not already in it
        """
        if obj not in self.list :
            obj.isComplete = False
            self.list.append(obj)
        
    def delObjective(self, obj) :
        """ obj : Objective
            removes 'obj' from the list if it's in it
        """
        if obj in self.list :
            obj.isComplete = True
            self.list.remove(obj)
        
    def getBestObjective(self) :
        """ returns : Objective, [(int,int)]
            selects the 3 objectives with the smallest 'value'
            runs A* for each and choses the one with the shortest path
        """
        pm = pathManager.PathManager(self.matrix)
        pm.setThreshold(self.threshold)
        sortedList = sorted(self.list, key = lambda o : o.value(self.position))
        #print sortedList
        minObj = None
        minDist = float('inf')
        minPath = None
        for obj in sortedList[:3] :
            pm.findPath(self.position, obj.goal)
            dist = pm.getPathLength() - obj.priority
            if dist < minDist :
                minDist = dist
                minObj = obj
                minPath = pm.path
        return minObj, minPath
    
    def getObjectives(self) :
        while len(self.list) > 0 :
            yield self.getBestObjective()
    
    def getNextPoint(self) :
        """ returns : Objective, (int,int)
            finds the best objective and the first point of the path to take
        """
        obj, path = self.getBestObjective()
        print path
        return obj, path[1]
    
    
    