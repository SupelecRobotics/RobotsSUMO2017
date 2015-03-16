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
import util
from robomoviesMapV2 import *


class Trajectoire :


    def __init__(self, coordinates, angle, orientation) :

        self.position = [coordinates, angle, orientation]
        
        self.currentWay = []

    def wololo(self, path) :
        # pas de changement d'orientation sur cette portion de trajectoire

        coor0 = self.position[0]
        angle0 = self.position[1]
        orientation = self.position[2]
        way = []
        
        for coor in path[1:] :
            dist = dist((x0,y0), coor)
            angle = angle0 + angle((x0, y0), coor)
            way.append(dist, angle, orientation)
            angle0 = angle
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
        
        return self.wololo(pouet.path)


traj = Trajectoire((20, 20), 0, True)

print traj.vaVoirLaBasSiJySuis((5, 8))
    
