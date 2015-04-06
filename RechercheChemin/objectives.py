# -*- coding: utf-8 -*-
"""
Created on Mon Feb 23 22:52:00 2015

@author: antoinemarechal
"""

# PRIORITYMANAGER POUR LES NULS

# A) POUR CREER UN OBJECTIF "FIXE"
#   ce type d'objectif a pour but de se trouver exactement sur un point
#   il est adapté aux objectifs se trouvant à proximité d'un mur et dont la localisation ne change pas 
#   1) créer un objet FixedObjective en précisant le point d'arrivée (coordonnées entières)
#   préciser également la priorité et le numéro du script associé à l'objectif

# B) POUR CREER UN OBJECTIF "MOBILE"
#   ce type d'objectif a pour but de se trouver face à un point, à une distance précise
#   il est adapté aux objectifs pouvant être approchés de tous côtés et dont la localisation peut changer
#   1) créer un objet MobileObjective en précisant le point d'arrivée (coordonnées quelconques) et la distance à atteindre
#   préciser également la priorité et le numéro du script associé à l'objectif

# C) POUR UTILISER LE GESTIONNAIRE D'OBJECTIFS
#   1) créer des objets de type FixedObjective et/ou MobileObjective (voir ci-dessus)
#   2) créer un objet de type PriorityManager
#   3) appeler la méthode add pour ajouter chaque objectif
#   4) modifier les attributs matrix, threshold, position en fonction de la situation actuelle
#   5) pour obtenir le chemin vers l'objectif optimal : appeler la méthode getBestObjective
#   6) pour obtenir le chemin reliant tout les objectifs, point par point (conseillé) :
#       a) appeler la méthode getNextPoint : renvoie le prochain objectif et le premier point
#       b) pour vérifier si l'objectif est atteint, regarder l'attribut isComplete
#       c) modifier l'attribut position pour refléter le déplacement
#       d) recommencer à a)

import util
import pathManager

class Objective :
    """ Implement an objective for the robot
        THIS CLASS IS FUCKING ABSTRACT DON'T YOU EVER THINK OF INSTANTIATING IT
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
        endX = round(f(endPoint[0],self.goal[0]), 3)
        endY = round(f(endPoint[1],self.goal[1]), 3)
        path.append((endX, endY))
        
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
        
    def add(self, obj) :
        """ obj : Objective
            adds 'obj' to the list if it's not already in it
        """
        if obj not in self.list :
            obj.isComplete = False
            self.list.append(obj)
        
    def remove(self, obj) :
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
        minDist = float('inf')
        minPath = None
        minObj = None
        for obj in sortedList[:3] :
            dist, path = obj.getPath(self.position, pm)
            if dist < minDist :
                minDist = dist
                minPath = path
                minObj = obj
        return minObj, minPath
    
    def getNextPoint(self) :
        """ returns : Objective, (int,int)
            finds the best objective and the first point of the path to take
        """
        obj, path = self.getBestObjective()
        #print path
        if len(path) <= 2 :
            self.remove(obj)
        return obj, path[1]
    
    
    