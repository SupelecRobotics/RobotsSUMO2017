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
from carte import Map
import serial
from calculAngle import *

class Robot :
    """ Simulates the Robot
    """

    def __init__(self, ser1, ser2, ser3) :
        self.com = com(ser1,ser2, ser3)
        #position physique
        self.x = 250
        self.y = 1000
        self.theta = 0
        self.dtheta = 0
        self.dx = -30
        self.dy = 0
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
        self.traj = traj((int(self.x), int(self.y)), self.theta, True)
        time.sleep(2)
        self.couleur = self.com.getColor()
        print self.couleur
        if self.couleur == 'V':
            self.dtheta = 0
            self.dx = 30
        self.com.envoiColor(self.couleur)
        time.sleep(2)
        self.com.envoiCouleurReady()
        self.printPosition()
        while not self.com.getGachette():
            time.sleep(1)
        self.com.envoiAllGreen()
        
        
        
    def bouge(self,d,theta):
        print self.com.envoiMain(d,theta)
        
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
        t = time.time()
        self.traj.detectionObstacles(self.com.getRobCoords())
        print "temps pris pour la detection d'obstacles " + str(time.time() - t)
        if(not self.traj.isInTheTravelableMap(point)) :
            print "point " + str(point) + " impossible à atteindre"
        else :
            print "From " + str((self.x, self.y)) + " to " + str(point)
            print self.traj.pointPath(point)
            print "start"
            for p in self.traj.pointPath(point):
                print "point"
                (a, b) = p
                (a, b) = (round(a), round(b))
                print "At : " + str((a, b))
                self.bougeToPoint((a, b))
            self.updatePosition()
        print "fin allerA"

            
    # def allerAangle(self, point,theta):
        # self.updatePosition()
     ##  self.traj.detectionObstacles(self.com.getRobCoords())
        # if(not self.traj.isInTheTravelableMap(point)) :
            # print "point " + str(point) + " impossible à atteindre"
        # else :
           ## tronquage dans trajectoire nécessaire?
            # print "From " + str((self.x, self.y)) + " to " + str(point)
            # print self.traj.pointPath(point)
            # print "start"
            # for p in self.traj.pointPath(point):
                # print "point"
                # (a, b) = p
                # (a, b) = (round(a), round(b))
                # print "At : " + str((a, b))
                # self.bougeToPoint((a, b))
            # self.bouge(0, int(theta - self.theta))
            # self.updatePosition()
            
    def allerAangle(self, point,theta):
        self.allerA(point)
        t = time.time()
        if(self.traj.isInTheTravelableMap(point)) :
            print "temps pris pour isInTheTravelableMap " + str(time.time() - t)
            self.bouge(0, int(theta - self.theta))
            self.updatePosition()
            
    def bougeToPoint(self,point):
        coor = (self.x,self.y)
        while dist(coor,point) > 70:     #100
            (distance, angle)  = self.orderToPoint(point)
            if (math.fabs(distance) > 500): distance = math.copysign(500,distance)
            self.bouge(0,int(angle))
            self.bouge(int(distance),0) #envoi d'entiers
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
        ang = (ang + 1800) % 3600 - 1800
        if (ang > 900): 
            ang = ang - 1800
            distance = -distance
        if (ang < -900):
            ang = ang + 1800
            distance = -distance
        return (distance, ang)

    
    def goToCylindreLocal(self, point, sens):
        self.updatePosition()
        (x0, y0) = (self.x,self.y)
        (x, y) = point
        distance = dist((x0,y0), point)
        ang = - self.theta + angle((1, 0), (x - x0, y - y0))*1800/math.pi
        
        (theta, L) = self.donneDonneesApproche(sens, int(distance / 10), False, ang)
        self.bouge(0,int(theta))
        time.sleep(0.5)
        self.bouge(int(L),0)
        time.sleep(0.5)
        if(sens):
            self.com.appelFermeturePinceDevant()
        else:
            self.com.appelFermeturePinceDerriere()
            
        
    def goToGobeletLocal(self, point, sens):
        self.face(point, sens)
        self.updatePosition()
        (x0, y0) = (self.x,self.y)
        (x, y) = point
        distance = dist((x0,y0), point)
        ang = - self.theta + angle((1, 0), (x - x0, y - y0))*1800/math.pi
        
        (theta, L) = self.donneDonneesApproche(sens, int(distance / 10), True, ang)
        self.bouge(0,int(theta))
        time.sleep(0.5)
        self.bouge(int(L),0)
        time.sleep(0.5)
        if(sens):
            self.com.appelMonteeActionneurGobeletDevant()
        else:
            self.com.appelMonteeActionneurGobeletDerriere()

    def donneAngleApproche(self, sens, l, gobelet) :
    #    sens : bool qui vaut true si l'objectif est devant le robot
    #    l : int égal à la distance centre robot à centre gobelet
    #    gobelet : bool vrai si l'objectif est un gobelet, et faux si c'est un plot
        
        #devant(gobelet, cylindre)
        d1 = 10
        d2 = 8.5
        #derriere(gobelet, cylindre)
        d3 = 9.5
        d4 = 8
        
        if (gobelet and sens):
            alpha = - math.asin(float(d1) / float(l))*360/(2*math.pi)
        elif (gobelet and not sens):
            alpha = math.asin(float(d3) / float(l))*360/(2*math.pi)
        elif (not gobelet and sens):
            alpha = math.asin(float(d2) / float(l))*360/(2*math.pi)
        else:
            alpha = - math.asin(float(d4) / float(l))*360/(2*math.pi)
        
        return alpha
        
        
    def donneLApproche(self, alpha, l, sens):
        profSpot = 7
        Lprime = abs(l * math.cos(float(alpha)*2*math.pi/360))
        L =  Lprime - 10 - float(profSpot) / float(2)
        
        return L
        
    def donneDonneesApproche(self, sens, l, gobelet, angle)    :
    #    sens : bool qui vaut true si l'objectif est devant le robot
    #    l : int égal à la distance centre robot à centre gobelet
    #    gobelet : bool vrai si l'objectif est un gobelet, et faux si c'est un plot
    #    angle : int (en déci-angle) angle qui permet de placer le robot dans la direction du gobelet/cylindre
        
        ## Constantes (en cm)
        
        #offset de la distance
        #devant(gobelet, cylindre)
        offset1 = 7.9
        offset2 = 8.2
        #derriere(gobelet, cylindre)
        offset3 = 7.9
        offset4 = 8.5
        
        #Distances au centre
        #devant(gobelet, cylindre)
        d1 = 9.9
        d2 = 8.5
        #derriere(gobelet, cylindre)
        d3 = 7.9
        d4 = 8
        
        if (gobelet and sens):
            alpha = - math.asin(float(d1) / float(l))*360/(2*math.pi)
        elif (gobelet and not sens):
            alpha = math.asin(float(d3) / float(l))*360/(2*math.pi)
        elif (not gobelet and sens):
            alpha = math.asin(float(d2) / float(l))*360/(2*math.pi)
        else:
            alpha = - math.asin(float(d4) / float(l))*360/(2*math.pi)
        
        # Lprime = abs(l * math.cos(float(alpha)*2*math.pi/360))
        # L =  Lprime - 10 - float(profSpot) / float(2)
        # L = L * 10 + 53
        
        L = abs(l * math.cos(float(alpha)*2*math.pi/360))
        if (gobelet and sens):
            L = (L - offset1) * 10
        elif (gobelet and not sens):
            L = (L - offset3) * 10
        elif (not gobelet and sens):
            L = (L - offset2) * 10
        else:
            L = (L - offset4) * 10
        
        theta =  alpha * 10 + angle
        if(not sens):
            theta += 1800
            theta = superModulo(theta)
            L = -L
        
        return (theta, L)
    
    
    # def goToGobelet(self, posGobelet)    :
        # self.updatePosition()
        # pathMan = PathManager(robomoviesForest.getForest())
        # pathMan.setThreshold(4)
        # (xG, yG) = posGobelet
        # (xG, yG) = ( (2000-y)/self.facteurDistance, x/self.facteurDistance)
        # print (xG,yG)
        # for i in range(1, 7)    :


            # pathMan.findPath((self.x, self.y),(xG, yG, 0))
            # length = pathMan.getPathLength()
        
        # print pouet



        
    def updatePosition(self):
        print "anciennes coords " + str((self.x, self.y))
        string = self.com.getInfos()
        self.x = round(string[0]) + self.dx
        print "dx " + str(self.dx)
        self.y = round(string[1]) + self.dy
        print "nouvelles coords " + str((self.x, self.y))
        self.theta = round(( (string[2] + self.dtheta + 1800 ) % 3600 ) - 1800) #( (string[2] + 1800 ) % 3600 ) - 1800   
        self.c1 = string[3]
        self.c2 = string[4]
        self.c3 = string[5]
        self.c4 = string[6]
        self.time = string[7]
        
        self.traj.updatePosition((self.x,self.y), self.theta, True)
        
    def gameD(self):
        #time.sleep(15)
        self.com.envoiDepartZone()
        if (self.couleur == 'J'):
            self.com.appelMonteeClapGauche()
            time.sleep(1)
        elif (self.couleur == 'V'):
            self.com.appelMonteeClapGauche()
            
    def game(self):
        try:
            self.gameFalse()
        except serial.SerialException:
            print "Cables Arduino déconnectés"
            self.com.envoiErreurArduino()
            
    def gameFalse(self):
        self.com.envoiDepartZone()
        if (self.couleur == 'J'):
            time.sleep(7)
            self.com.appelOuvertureExternePinceDevant()
            self.com.appelOuvertureExternePinceDerriere()
            self.allerA((650, 1000)) #pour ne pas se prendre le bord en sortant...
            self.goToGobeletLocal((910, 1170), False)
            self.allerA((870, 1000))
            #   self.goToCylindreLocal((870, 645), True)
            self.allerA((450, 450))
            self.goToGobeletLocal((250, 250), True)
            self.allerAangle((300,280),-900)
            self.com.appelDescenteClapDroit()
            self.allerAangle((300,280),0)
            self.com.appelMonteeClapDroit()
            self.allerAangle((700, 280), 0)
            self.com.appelDescenteClapDroit()
            self.bouge(200, 0)
            self.bouge(60, 0)
            self.com.appelMonteeClapDroit()
            self.goToCylindreLocal((1100,230),True)
            self.bouge(200,0)
            self.allerAangle((600, 1000), 0)
            self.allerA((400, 1000))
            self.com.appelDescenteActionneurGobeletDevant()
            self.com.appelOuvertureExternePinceDevant()
            self.allerA((550,1000))
            self.allerAangle((2400,300),-900)
            self.com.appelDescenteClapGauche()
            self.allerAangle((2400,300),-1750)
            self.com.appelMonteeClapGauche()
            self.allerAangle((2500,700),0)
            self.com.appelDescenteActionneurGobeletDevant()
            self.allerA((1600,650))
            self.goToGobeletLocal((1500,350),True)
            self.allerAangle((400,1600),450)
            self.com.appelDescenteActionneurGobeletDevant()
            self.com.appelDescenteActionneurGobeletDerriere()
        elif (self.couleur == 'V'):
            time.sleep(7)
            self.com.appelOuvertureExternePinceDerriere()
            self.com.appelOuvertureExternePinceDevant()
            self.allerA((2350,1000))
            self.goToGobeletLocal((2090, 1170), False)
            #self.allerA((2130, 1000))
            # self.goToCylindreLocal((2130, 645), True)
            self.allerA((2550, 450))
            self.goToGobeletLocal((2750, 250), True)
            self.allerAangle((int(2700),int(280)),-900)
            self.com.appelDescenteClapGauche()
            self.allerAangle((int(2700),int(280)), -1800)
            self.com.appelMonteeClapGauche()
            self.allerAangle((int(2300),int(280)), -1800)
            self.com.appelDescenteClapGauche()
            self.bouge(200, 0)
            self.bouge(60,0)
            self.com.appelMonteeClapGauche()
            self.goToCylindreLocal((1900,230),True)
            self.bouge(200,0)
            self.allerAangle((2400, 1000), 0)
            self.allerA((2600, 1000))
            self.com.appelDescenteActionneurGobeletDevant()
            self.com.appelOuvertureExternePinceDevant()
            self.allerA((2450,1000))
            self.allerAangle((600,300),-900)
            self.com.appelDescenteClapDroit()
            self.allerAangle((600,300),0)
            self.com.appelMonteeClapDroit()
            self.allerAangle((500,700),-1800)
            self.com.appelDescenteActionneurGobeletDevant()
            self.allerA((1400,650))
            self.goToGobeletLocal((1500,350),True)
            self.allerAangle((2600,1600),2250)
            self.com.appelDescenteActionneurGobeletDevant()
            self.com.appelDescenteActionneurGobeletDerriere()

    def printPosition(self):
        # Demande des informations récentes à l'arduino puis
        # affiche les informations stockées dans les variables du robot.
        self.updatePosition()
        print "x : " + str(self.x) + " , y : " + str(self.y) + " , theta : " + str(self.theta)
        print "Capteurs : " + str(self.c1) + " ; " + str(self.c2) + " ; " + str(self.c3) + " ; " + str(self.c4) 
        print "time : " + str(self.time)
        
    def printPositionRobot(self):
        # affiche les informations stockées dans les variables du robot
        # Attention !!! les informations ne sont pas nécessairement récentes.
        print "x : " + str(self.x) + " , y : " + str(self.y) + " , theta : " + str(self.theta)
        print "Capteurs : " + str(self.c1) + " ; " + str(self.c2) + " ; " + str(self.c3) + " ; " + str(self.c4) 
        print "time : " + str(self.time)

    def isFacing(self, x, y) :
        dx = x - self.x
        dy = y - self.y
        dtheta = (1800/math.pi) * math.atan2(dy,dx) - self.theta
        dtheta = dtheta % 3600
        return (dtheta < 900 or dtheta > 2700)
        
    def face(self, point, sens) :
        (x, y) = point
        self.updatePosition()
        dx = x - self.x
        dy = y - self.y
        dtheta = - self.theta + angle((1, 0), (dx, dy))*1800/math.pi
        if(not sens) :
            dtheta += 1800
        dtheta = superModulo(dtheta)
        self.bouge(0, int(dtheta))
        
        
    def evasionObstacle(self):
        #distance du robot à l'osbtacle (estimée)   
        obstacleDevant = (self.c2 <= 30 and self.c3 <= 30)
        d = 10
        alpha = int(self.theta / 10)
        pointDevant = (int(self.x + d * Math.cos(alpha)), int(self.y + d * Math.sin(alpha)))
        pointDroite = (int(self.x + d * Math.cos(alpha-90)), int(self.y + d * Math.sin(alpha-90)))
        pointGauche = (int(self.x + d * Math.cos(alpha+90)), int(self.y + d * Math.sin(alpha+90)))
        pointDerriere = (int(self.x + d * Math.cos(alpha+180)), int(self.y + d * Math.sin(alpha+180)))
    
    
        
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








