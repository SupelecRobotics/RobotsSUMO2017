# -*- coding: utf-8 -*-
"""
Created on Mon Feb 23 22:52:00 2015

@author: antoinemarechal
"""

import util
import pathManager

class Objective :
    """ Implement an objective for the robot
        THIS CLASS IS FUCKING ABSTRACT DON'T YOU EVER THINK OF IMPLEMENTING IT
    """
    
    def __init__(self, priority, script) :
        """ priority : int, script : int
            AGAIN THIS CLASS IS ABSTRACT YOU BETTER NOT CALL THIS CONSTRUCTOR
        """
        self.priority = priority
        self.script = script
        self.isComplete = False
    
    # METHODS DEFINED IN ALL DERIVED CLASSES
    
    # def value(self, position) : 
    #   position : (float,float)
    #   returns : int
    
    # def getPath(self, position, pm) :
    #   position : (int,int)
    #   pm : PathManager
    #   returns : float, [(float,float)]

class FixedObjective(Objective) :
    """ The objective is to be on a given point (at a given orientation?)
    """
    
    def __init__(self, goal, priority, script) :
        """ goal : (int,int), priority : int, script : int
        """
        Objective.__init__(self, priority, script)
        self.goal = goal
    
    def value(self, position) :
        return util.dist(self.goal, position) - self.priority
    
    def getPath(self, position, pm) :
        goal = self.goal + (0,) 
        pm.findPath(position, goal)
        dist = pm.getPathLength() - self.priority
        path = pm.path
        return dist, path
    
class MobileObjective(Objective) :
    """ The objective is to face a given point at a given distance
    """
    
    def __init__(self, goal, distance, priority, script) :
        """ goal : (float,float), distance : float, priority : int, script : int
        """
        Objective.__init__(self, priority, script)
        self.goal = goal            # may be accessed directly
        self.distance = distance
    
    def value(self, position) :
        return util.dist(self.goal, position) - self.distance - self.priority
    
    def getPath(self, position, pm) :
        goal = self.goal + (self.distance+2,)
        pm.findPath(position, goal)
        
        path = pm.path
        endPoint = path[len(path)-1]
        f = lambda a,b : b + (a-b)*self.distance/util.dist(endPoint, self.goal)
        newEndPoint = (f(endPoint[0],self.goal[0]), f(endPoint[1],self.goal[1]))
        path.append(newEndPoint)
        
        dist = pm.getPathLength()
        return dist, path

        

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
    
    
    