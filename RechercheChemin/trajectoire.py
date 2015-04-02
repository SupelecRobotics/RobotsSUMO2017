# -*- coding: utf-8 -*-
"""
Created on Mon Nov 03 23:08:08 2014
@author: christianhamelain
"""

##import random
##
import math
##
##import os

from pathManager import PathManager
from util import *
from robomoviesMapV2 import *


class Trajectoire :


    def __init__(self, coordinates, angle, orientation) :

        self.position = [coordinates, angle, orientation]
        
        self.currentWay = []

        self.facteurDistance = 50

        self.facteurDegre = 10

    def wololo(self, path) :
        # pas de changement d'orientation sur cette portion de trajectoire

        coor0 = self.position[0]
        angle0 = self.position[1]
        orientation = self.position[2]
        way = []
        
        for coor in path[1:] :
            (x0, y0) = coor0
            (x, y) = coor
            distance = dist(coor0, coor)
            ang = - angle0 + angle((0, 1), (x - x0, y - y0))
            ang = (ang + math.pi) % (2*math.pi)  - math.pi     # ang dans [-180, 180]
            way.append((distance*self.facteurDistance, ang*180/math.pi*self.facteurDegre, orientation)) 
            angle0 = ang
            coor0 = coor

        self.currentWay = way
        
        return way

    

    def vaVoirLaBasSiJySuis(self, point) :

        pouet = PathManager(robomoviesForest.getForest())
        pouet.setThreshold(4)
        (x, y) = point
        pouet.findPath(self.position[0],(x, y, 0))

        print "path"
        print pouet.path

        wolo = self.wololo(pouet.path)

        for coor in pouet.path :
            (x, y) = coor
            robomoviesForest.forest[x][y] = -8

        robomoviesForest.displayForest()
        
        return wolo

#robomoviesForest.displayForest()

traj = Trajectoire((20, 5), 0, True)

pouet = traj.vaVoirLaBasSiJySuis((6, 50))

print pouet


    
