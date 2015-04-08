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
        
        (x,y) = coordinates
        
        self.currentWay = []

        self.facteurDistance = 50.0

        self.facteurDegre = 10.0
        
        self.position = [( (2000-y)/self.facteurDistance, x/self.facteurDistance), angle/self.facteurDegre*math.pi/180, orientation]

#        print self.position

    def chemin(self, path) :
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
#            print angle0
#            print angle((0, 1), (x - x0, y - y0))
            ang = (ang + math.pi) % (2*math.pi)  - math.pi     # ang dans [-180, 180]
            way.append((0, ang*180/math.pi*self.facteurDegre, orientation)) 
            way.append((distance*self.facteurDistance, 0, orientation)) 
            angle0 = ang
            coor0 = coor

        self.currentWay = way
        
        return way

    def comingOut(self, point, angleArrivee)   :

        pathMan = PathManager(robomoviesForest.getForest())
        pathMan.setThreshold(4)
        (x, y) = point
        (x, y) = ( (2000-y)/self.facteurDistance, x/self.facteurDistance)
        pathMan.findPath(self.position[0],(x, y, 0))

        path = pathMan.path
        
        coor0 = self.position[0]
        angle0 = self.position[1]
        orientation = self.position[2]
        way = []

              
        for coor in path[1:] :
            (x0, y0) = coor0
            (x, y) = coor
            distance = dist(coor0, coor)
            ang = - angle0 + angle((1, 0), (x - x0, y - y0))
            ang = (ang + math.pi) % (2*math.pi)  - math.pi     # ang dans [-180, 180]
            way.append((distance*self.facteurDistance, ang*180/math.pi*self.facteurDegre, orientation)) 
            angle0 = ang
            coor0 = coor

        (x0, y0) = path[-2]
        (x1, y1) = path[-1]
        ang = - angle((1, 0), (x1 - x0, y1 - y0)) + angleArrivee
        ang = (ang + math.pi) % (2*math.pi)  - math.pi     # ang dans [-180, 180]
        way.append((0, ang*180/math.pi*self.facteurDegre, orientation)) 
        
        self.currentWay = way


        return way


        

    def ordersTo(self, point) :

        pathMan = PathManager(robomoviesForest.getForest())
        pathMan.setThreshold(4)
        (x, y) = point
        (x, y) = ( (2000-y)/self.facteurDistance, x/self.facteurDistance)
        print (x,y)
        pathMan.findPath(self.position[0],(x, y, 0))

#        print "path"
#        print pathMan.path

        way = self.chemin(pathMan.path)

        for coor in pathMan.path :
            (x, y) = coor
            robomoviesForest.forest[int(x)][int(y)] = -8

#        robomoviesForest.displayForest()
        
        return way
        
        
    def pointPath(self, point) :

        pathMan = PathManager(robomoviesForest.getForest())
        pathMan.setThreshold(4)
        (x, y) = point
        (x, y) = ( (2000-y)/self.facteurDistance, x/self.facteurDistance)
        print (x,y)
        pathMan.findPath(self.position[0],(x, y, 0))

#        print "path"
#        print pathMan.path

        pth = []
        for coor in pathMan.path:
            (x,y) = coor            
            pth.append( (y*self.facteurDistance ,(40-x)*self.facteurDistance) )
        
        return pth
        
    def orderToPoint(self, point):
        (x0, y0) = (500,1000)
        (x, y) = point
        distance = dist((x0,y0), point)
        print angle((1, 0), (x - x0, y - y0))*180/math.pi
        ang = - 0 + angle((1, 0), (x - x0, y - y0))*180/math.pi
        ang = (ang + 180) % (360)  - 180     # ang dans [-180, 180]
        return (distance, ang)

#robomoviesForest.displayForest()
#
#traj = Trajectoire((250, 1000), 0, True)
#
#pouet = traj.pointPath((1500, 350))
#commande = traj.orderToPoint((700,1700))
#
#print pouet
#print commande


    
