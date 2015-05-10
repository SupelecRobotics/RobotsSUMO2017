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
from robomoviesMapLoad import *
from CommunicationSerial import CommunicationSerial as com


        
class Trajectoire :


    def __init__(self, coordinates, angle, orientation) :
        
        self.currentWay = []
        
        
        
        self.facteurDistance = 10.0
        # avant 50

        self.facteurDegre = 10.0
        
        self.position = []
        self.updatePosition(coordinates, angle, orientation)
        
        self.pm = PathManager(robomoviesForest)
        self.pm.setThreshold(4)

#        print self.position
    
    def updatePosition(self, coordinates, angle, orientation) :
        
        (x, y) = coordinates
        self.position = [ ((2000 - y) / self.facteurDistance, x / self.facteurDistance), (math.pi/180) * angle / self.facteurDegre, orientation ]
    
    def detectionObstacles(self, pointVersionComBalise):
        print 'getRobCoords Start'
        (x, y) = pointVersionComBalise
        print 'detection'
        print (x, y)
        pointVersionForest = (x / 10, 300 - y / 10)
        print 'sur la Forest'
        print pointVersionForest
        robomoviesForest.loadTextFile('/home/pi/RobotsSUMO2017/RobotCoupe/newMap-Original.txt')
        robomoviesForest.popLosange(pointVersionForest, 38, -1)
        robomoviesForest.popLosange(pointVersionForest, 13, 0)
        #debug
        robomoviesForest.createTextFile('/home/pi/RobotsSUMO2017/RobotCoupe/newMap.txt')
        print 'fin de creation d obstacle'

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

        (x, y) = point
        (x, y) = ( (2000-y)/self.facteurDistance, x/self.facteurDistance)
        self.pm.findPath(self.position[0],(x, y, 0))

        path = self.pm.path
        
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

        (x, y) = point
        (x, y) = ( (2000-y)/self.facteurDistance, x/self.facteurDistance)
        print (x,y)
        self.pm.findPath(self.position[0],(x, y, 0))

#        print "path"
#        print self.pm.path

        way = self.chemin(self.pm.path)

        for coor in self.pm.path :
            (x, y) = coor
            robomoviesForest.forest[int(x)][int(y)] = -8

#        robomoviesForest.displayForest()
        
        return way
        
        
    def pointPath(self, point) :

        (x, y) = point
#        print (x,y)
        (x, y) = ( round( (2000-y)/self.facteurDistance), round(x/self.facteurDistance))
        print (x,y)
        self.pm.findPath(self.position[0],(x, y, 0))

#        print "path"
#        print self.pm.path

        pth = []
        for coor in self.pm.path:
            (x,y) = coor            
            pth.append( (y*self.facteurDistance ,(2000/self.facteurDistance-x)*self.facteurDistance) )
        
        return pth
        
        
    def orderToPoint(self, point):
        (x0, y0) = (450,1000)
        (x, y) = point
        distance = dist((x0,y0), point)
        print angle((1, 0), (x - x0, y - y0))*1800/math.pi
        ang = - 600 + angle((1, 0), (x - x0, y - y0))*1800/math.pi
        print ang
      #  ang = ang % 3600     # ang dans [-180, 180]
        return (distance, ang)

#robomoviesForest.displayForest()
##
#traj = Trajectoire((450, 1000), 0, True)
##
#pouet = traj.pointPath((600, 800))
##commande = traj.orderToPoint((350,800))
##
#print pouet
#print commande


    
