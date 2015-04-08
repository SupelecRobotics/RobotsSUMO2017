# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 19:39:38 2015

@author: Fabien
"""
import time
from util import *
from CommunicationSerial import CommunicationSerial as com
from trajectoire import Trajectoire as traj

class Robot :
    """ Simulates the Robot
    """
    
    def __init__(self, ser1, ser2) :
        self.com = com(ser1,ser2)
        #position physique
        self.x = 250
        self.y = 1000
        self.theta = 0
        # capteurs
        self.c1 = 0
        self.c2 = 0
        self.c3 = 0
        self.c4 = 0
        #time
        self.time = 0
        time.sleep(3)
        
    def bouge(self,d,theta):
        self.com.envoiMoteurCapteur(d,theta)
        
#    def bougeAngle(self,angle):
#        while self.theta - angle > 3:
#            self.printPosition()
#            coor = (self.x, self.y)
#            (x, y) = point
#            distance = dist(coor, point)
#            ang = - self.theta + angle((x, 0), (x - self.x, y - self.y))
#            ang = (ang + math.pi) % (2*math.pi)  - math.pi     # ang dans [-180, 180]
#            print int(distance)
#            print int(ang*10)
#            self.com.envoiMoteurCapteur(int(distance),int(ang*10)) #envoi d'entiers
#            time.sleep(0.5)
        
    def allerA(self, point):
        trajectoire = traj((self.x, self.y), self.theta, True)
        print point
        print "debut"
#        print trajectoire.orderToPoint(point)
        for point in trajectoire.pointPath(point):
            print point
            self.bougeToPoint(point)
            time.sleep(0.1)
            
    def bougeToPoint(self,point):
        print "objective : " + str(point) 
        coor = (self.x,self.y)
        while dist(coor,point) > 50:
            self.printPosition()
            (distance, angle)  = self.orderToPoint(point)
            if (distance > 900): distance = 900
            print (distance, angle)
            coor = (self.x, self.y)
            self.com.envoiMoteurCapteur(0,int(angle))
            time.sleep(0.1)
            self.com.envoiMoteurCapteur(int(distance),0) #envoi d'entiers
            time.sleep(0.1)
            
    def orderToPoint(self, point):
        (x0, y0) = (self.x,self.y)
        (x, y) = point
        distance = dist((x0,y0), point)
        ang = - self.theta + angle((1, 0), (x - x0, y - y0))*1800/math.pi
        if (ang > 900): 
            ang = ang - 1800
            distance = -distance
        if (ang < -900):
            ang = ang + 1800
            distance = -distance
        return (distance, ang)
        
    def updatePosition(self):
        string = self.com.getInfos()
        self.x = string[0]
        self.y = string[1]
        self.theta = string[2]
        self.c1 = string[3]
        self.c2 = string[4]
        self.c3 = string[5]
        self.c4 = string[6]
        
    def printPosition(self):
        self.updatePosition()
        print "x : " + str(self.x) + " , y : " + str(self.y) + " , theta : " + str(self.theta)
        print "Capteurs : " + str(self.c1) + " ; " + str(self.c2) + " ; " + str(self.c3) + " ; " + str(self.c4) 
