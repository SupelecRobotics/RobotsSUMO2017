# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 19:39:38 2015

@author: Fabien
"""
import time
from CommunicationSerial import CommunicationSerial as com

class Robot :
    """ Simulates the Robot
    """
    
    def __init__(self, ser1, ser2) :
        self.com = com(ser1,ser2)
        #position physique
        self.x = 0
        self.y = 0
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