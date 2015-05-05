# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 19:39:38 2015

@author: Fabien
"""
import time
import math
from util import *
from pathManager import PathManager
from robomoviesMapLoad import *
from CommunicationSerial import CommunicationSerial as com
from trajectoire import Trajectoire as traj
import serial

class Robot :
    """ Simulates the Robot
    """
    
    def __init__(self, ser1, ser2, ser3) :
		self.com = com(ser1,ser2, ser3)
        #position physique
		self.x = 250
		self.y = 1000
		self.theta = 0
        # capteurs
		self.c1 = 0
		self.c2 = 0
		self.c3 = 0
		self.c4 = 0
		#changement de repère
		self.facteurDistance = 10.0
		self.facteurDegre = 10.0
		#time
        self.time = 0
        time.sleep(2)
        self.couleur = self.com.getColor()
        print self.couleur
        self.com.envoiColor(self.couleur)
        time.sleep(2)
        self.com.envoiCouleurReady()
        self.printPosition()
        while self.com.getGachette() != True :
            time.sleep(1)
        self.com.envoiAllGreen()
		
        
    def bouge(self,d,theta):
        self.com.envoiMain(d,theta)
        
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
        self.updatePosition()
        trajectoire = traj((self.x, self.y), self.theta, True)
        print "From " + str((self.x, self.y)) + " to " + str(point)
#        print trajectoire.orderToPoint(point)
        for point in trajectoire.pointPath(point):
            print "At : " + str(point)
            self.bougeToPoint(point)
            
    def allerAangle(self, point,theta):
        self.updatePosition()
        #tronquage dans trajectoire nécessaire?
        trajectoire = traj((self.x, self.y), self.theta, True)
        print "From " + str((self.x, self.y)) + " to " + str(point)
#        print trajectoire.orderToPoint(point)
        for point in trajectoire.pointPath(point):
            print "At : " + str(point)
            self.bougeToPoint(point)
        self.bouge(0, theta - self.theta)
#        if (math.fabs(theta - self.theta) <= 1800 ):
#            self.bouge(0, theta - self.theta)
#        else:
#            self.bouge(0, theta - self.theta - 3600)
            
    def bougeToPoint(self,point):
        coor = (self.x,self.y)
        while dist(coor,point) > 30: 	#100
            (distance, angle)  = self.orderToPoint(point)
            if (math.fabs(distance) > 500): distance = math.copysign(500,distance)
            self.com.envoiMain(0,int(angle))
            self.com.envoiMain(int(distance),0) #envoi d'entiers
            self.printPosition()
            coor = (self.x, self.y)
            
#    def bougeToPoint(self,point):
#        (distance, angle)  = self.orderToPoint(point)
#        self.com.envoiMain(0,int(angle))
#        while math.fabs(distance) > 500:
#            self.com.envoiMain(int(math.copysign(500,distance)),0)
#            distance -= math.copysign(500,distance)
#        self.com.envoiMain(int(distance),0) #envoi d'entiers
#        self.printPosition()
            
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
        
    def goToGobeletLocal(self, point):
        robot.updatePosition()
        (x0, y0) = (self.x,self.y)
        (x, y) = point
        distance = dist((x0,y0), point)
        ang = - self.theta + angle((1, 0), (x - x0, y - y0))*1800/math.pi
        orientationInitiale = True
        sens = True
        robot.printPosition()
        l = distance / 10
        d1 = 10
        d2 = 30
        gobelet = True
        theta = donneAlpha(orientationInitiale, bool(sens), int(l), d1, d2, gobelet)
        print theta
        profSpot = 7
        L = donneL(theta, int(l), profSpot)
        L = L * 10
        theta =  theta * 10 + ang
        robot.bouge(0,int(theta))
        time.sleep(1)
        robot.bouge(int(L),0)
        robot.com.appelMonteeActionneurGobeletDevant()
        time.sleep(2)
        robot.com.appelDescenteActionneurGobeletDevant()
		
	def goToGobelet(self, posGobelet)	:
		
		self.updatePosition()
		pathMan = PathManager(robomoviesForest.getForest())
        pathMan.setThreshold(4)
        (xG, yG) = posGobelet
        (xG, yG) = ( (2000-y)/self.facteurDistance, x/self.facteurDistance)
        print (xG,yG)
		for i in range(1, 7)	:
			
			
			pathMan.findPath((self.x, self.y),(xG, yG, 0))
			length = pathMan.getPathLength()
			
		
		
		
        
    def updatePosition(self):
        string = self.com.getInfos()
        self.x = string[0]
        self.y = string[1]
        self.theta = string[2] #( (string[2] + 1800 ) % 3600 ) - 1800
        self.c1 = string[3]
        self.c2 = string[4]
        self.c3 = string[5]
        self.c4 = string[6]
        self.time = string[7]
        
    def gameD(self):
        #time.sleep(15)
        self.com.envoiDepartZone()
        if (self.couleur == 'J'):
            self.allerAangle((int(220),int(550)), int(-900))
#            time.sleep(2)
#            robot.allerAangle((int(650),int(1100)), int(0))
#            time.sleep(2)
#            robot.allerAangle((int(1250),int(450)), int(1800))
#            time.sleep(2)
#            robot.allerAangle((int(2600),int(250)), int(1800))
#            time.sleep(2)
#            robot.allerAangle((int(2600),int(600)), int(0))
#            time.sleep(2)
#            robot.allerAangle((int(2300),int(600)), int(0))
#            time.sleep(2)
#            robot.allerAangle((int(2700),int(1400)), int(1800))
#            time.sleep(2)
#            robot.allerAangle((int(1500),int(1000)), int(1800))
#            time.sleep(1)
        
#            self.allerAangle((int(300),int(550)), int(-1170))
#            time.sleep(1)
#            self.bouge(150,0)
            #robot.com.appelActionneurMonteeGobeletDevant()
#            time.sleep(1)
#            self.bouge(-150,0)
#            time.sleep(1)
            self.allerAangle((int(250),int(250)), int(-900))
            self.com.appelDescenteClapDroit()
            self.allerAangle((int(250),int(250)), int(0))
#            self.bouge(100,0)
            self.com.appelMonteeClapDroit()
            self.allerAangle((int(850),int(250)), int(-900))
            self.com.appelDescenteClapDroit()
            self.allerAangle((int(850),int(250)), int(0))
#            self.bouge(100,0)
            self.com.appelMonteeClapDroit()
            # fait claps
            
#            self.allerAangle((int(600),int(1000)), int(1800))
#            #robot.com.appelDescenteGobeletDevant()
            self.allerAangle((int(2600),int(250)), int(1800))
            self.com.appelDescenteClapGauche()
#            self.bouge(0,-500)
#            self.bouge(0,500)
#            self.bouge(200,0)
            self.com.appelMonteeClapGauche()
            time.sleep(1)
        elif (self.couleur == 'V'):
#            self.allerAangle((int(2700),int(550)), int(-800))
#            time.sleep(1)
#            self.bouge(150,0)
            self.allerAangle((int(2750),int(250)), int(0))
            self.com.appelDescenteClapDroit()
            self.allerAangle((int(2750),int(250)), int(-900))
            self.com.appelMonteeClapDroit()
            self.allerAangle((int(2150),int(250)), int(0))
            self.com.appelDescenteClapDroit()
            self.allerAangle((int(2150),int(250)), int(-900))
            self.com.appelMonteeClapDroit()
            
#            self.allerAangle((int(600),int(1000)), int(1800))
#            #robot.com.appelDescenteGobeletDevant()
            self.allerAangle((int(400),int(250)), int(0))
            self.com.appelDescenteClapGauche()
#            self.bouge(0,500)
#            self.bouge(0,-500)
#            self.bouge(200,0)
            self.com.appelMonteeClapGauche()
            
#            robot.allerAangle((int(2780),int(550)), int(-900))
#            time.sleep(2)
#            robot.allerAangle((int(2350),int(1100)), int(1800))
#            time.sleep(2)
#            robot.allerAangle((int(1750),int(450)), int(0))
#            time.sleep(2)
#            robot.allerAangle((int(400),int(250)), int(0))
#            time.sleep(2)
#            robot.allerAangle((int(400),int(600)), int(1800))
#            time.sleep(2)
#            robot.allerAangle((int(700),int(600)), int(1800))
#            time.sleep(2)
#            robot.allerAangle((int(400),int(1400)), int(0))
#            time.sleep(2)
#            robot.allerAangle((int(800),int(1400)), int(0))
#            time.sleep(1)
            
    def game(self):
        try:
            self.gameD()
        except serial.SerialException:
            print "Cables Arduino déconnectés"
            self.com.envoiErreurArduino()
            
    def gameFalse(self):
        self.com.envoiDepartZone()
        if (self.couleur == 'J'):
            self.allerAangle((int(250),int(250)),-900)
            self.com.appelDescenteClapDroit()
            self.allerAangle((int(250),int(250)), 0)
            self.com.appelMonteeClapDroit()
        elif (self.couleur == 'V'):
            self.allerAangle((int(2750),int(250)),-900)
            self.com.appelDescenteClapGauche()
            self.allerAangle((int(2750),int(250)), -1800)
            self.com.appelMonteeClapGauche()
        
    def printPosition(self):
        self.updatePosition()
        print "x : " + str(self.x) + " , y : " + str(self.y) + " , theta : " + str(self.theta)
        print "Capteurs : " + str(self.c1) + " ; " + str(self.c2) + " ; " + str(self.c3) + " ; " + str(self.c4) 
        print "time : " + str(self.time)

    def isFacing(self, x, y) :
        dx = x - self.x
        dy = y - self.y
        dtheta = (1800/math.pi) * math.atan2(dy,dx) - self.theta
        dtheta = dtheta % 3600
        return (dtheta < 900 or dtheta > 2700)
    

"""

# OBTENTION DES CHEMINS

# parametres necessaires
matrix = [[?]] # la carte du terrain

clap1 = (?,?) #
clap2 = (?,?) # position des claps
clap3 = (?,?) #

gobelet1 = (?,?) #
gobelet2 = (?,?) # position des gobelets
gobelet3 = (?,?) #

distanceGobelet = ? # distance voulue entre le centre du robot et le gobelet au debut du script

# obtention des chemins
pm = PathManager(matrix)

obj = FixedObjective(clap1, 0, 0) # cette variable est ecrasee a chaque nouvel objectif
pathC1 = obj.getPath(robot.position, pm)[1] # chemin vers le clap 1
# cette ligne peut etre repetee pour obtenir le chemin depuis une nouvelle position. Pas besoin de repeter la ligne precedente tant que l'objectif reste le meme.

obj = FixedObjective(clap2, 0, 0)
pathC2 = obj.getPath(robot.position, pm)[1] # chemin vers le clap 2

obj = FixedObjective(clap3, 0, 0)
pathC3 = obj.getPath(robot.position, pm)[1] # chemin vers le clap 3

obj = MobileObjective(gobelet1, distanceGobelet, 0, 0)
pathG1 = obj.getPath(robot.position, pm)[1] # chemin vers le gobelet 1

obj = MobileObjective(gobelet2, distanceGobelet, 0, 0)
pathG2 = obj.getPath(robot.position, pm)[1] # chemin vers le gobelet 2

obj = MobileObjective(gobelet3, distanceGobelet, 0, 0)
pathG3 = obj.getPath(robot.position, pm)[1] # chemin vers le gobelet 3

# /!\ remplacer "robot.position" par le bon moyen d'obtenir la position du robot /!\

"""








