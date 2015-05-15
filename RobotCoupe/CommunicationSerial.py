# -*- coding: utf-8 -*-
"""
Created on Thu Mar 05 22:08:01 2015

@author: Fabien
"""

import serial # bibliothèque permettant la communication série
import time # pour le délai d'attente entre les messages

class CommunicationSerial :
    """ Links the Raspberry Pi with Arduinos through Serial Communication
    """

    def openSerial(self, serPath):

        try:
            ser = serial.Serial(serPath, 115200)
        except serial.SerialException:
            print "No connection to the device " + serPath + " could be established"
            return None
        else:
            print "Serial " + serPath + " successfully opened"
            return ser

        
    def sendIdQueries(self, serials):

        for ser in serials:

            if(ser is not None):
                print "Sending to " + ser.port
                ser.write(chr(250))
            else:
                print "Serial not opened, cannot send query"
                
        time.sleep(3)


    def identifySerial(self, ser):     
        if(ser is not None):
            print "Receiving from " + ser.port
            a = ser.read()
            ser.readline()
            print "Serial reads : " + a.encode('hex')

            if (a.encode('hex') == '00'): self.serMain = ser
            elif (a.encode('hex') == '01'): self.serCouleur = ser
            else: self.serBluetooth = ser
        else:
            print "Serial not opened, cannot read Id code"
    
    def __init__(self, ser1, ser2, ser3) :

        
        sera = self.openSerial(ser1)
        serb = self.openSerial(ser2)
        serc = self.openSerial(ser3)

        print '\n'

        time.sleep(3)

        print "Sending Id queries..."
        #self.sendIdQueries([sera])
        self.sendIdQueries([sera,serb,serc])

        print '\n'
        print "Receiving Id codes..."
        
        self.serMain = None
        self.serCouleur = None
        self.serBluetooth = None
        
        self.identifySerial(sera)
        self.identifySerial(serb)
        self.identifySerial(serc)
        
        time.sleep(2)

        self.lastRobCoords = [(0,0),(0,0)]
        self.trackingStat = [0,0]
        
    def envoiMain(self, d=0, theta=0):
        # commande sur 1 byte, distance sur 2 bytes, theta sur 2 bytes, 
        commande = 0
        if (d<0):
           d = -d + 32768
        d1 = d >> 8
        d2 = d - (d1 << 8)
        if (theta<0): 
            theta = -theta + 32768
        t1 = theta >> 8
        t2 = theta - (t1 << 8)
        satVitesse = 230    #saturation vitesse : 1 byte max
        
        inputByteString = chr(commande) + chr(d1) + chr(d2) + chr(t1) + chr(t2) + chr(satVitesse)
        print "envoi"
        print d
        print theta
        self.serMain.write(inputByteString)
        if (self.serMain.read().encode('hex') == '02'):
            return False
        self.serMain.readline()
        print "reçu"
        return True
    
    def getRobCoords(self):
        
        if(self.serBluetooth is not None) :
            while(self.serBluetooth.inWaiting() > 0):
                c = ''
                while(c != '#'):
                    c = self.serBluetooth.read()
                    print "first loop"

                msg = self.serBluetooth.read(10)
                print msg

                if(msg[9].isdigit()):
                    camIndex = int(msg[9]) - 1

                    if(msg[1] == 'x'):
                        self.trackingStat[camIndex] = 0
                    elif(msg[1:9].isdigit()):
                        self.trackingStat[camIndex] = 1
                        self.lastRobCoords[camIndex] = ((int(msg[1:5]),int(msg[5:-1])))


            nbValidCams = self.trackingStat[0] + self.trackingStat[1]

            if(nbValidCams > 0):
                x = (self.trackingStat[0]*self.lastRobCoords[0][0] + self.trackingStat[1]*self.lastRobCoords[1][0])/nbValidCams
                y = (self.trackingStat[0]*self.lastRobCoords[0][1] + self.trackingStat[1]*self.lastRobCoords[1][1])/nbValidCams
                return (x,y)
            else:
                return None
        else :
            print "Bluetooth Arduino Disconnected"
            return None
        
    def envoiMainSat(self, d=0, theta=0, satVitesse=0):
        commande = 0
        if (d<0):
           d = -d + 32768
        d1 = d >> 8
        d2 = d - (d1 << 8)
        if (theta<0): 
            theta = -theta + 32768
        t1 = theta >> 8
        t2 = theta - (t1 << 8)
        satV = satVitesse - ((satVitesse >> 8) << 8)    #saturation vitesse : 1 byte max
        
        inputByteString = chr(commande) + chr(d1) + chr(d2) + chr(t1) + chr(t2) + chr(satV)
        self.serMain.write(inputByteString)            
        self.serMain.readline()
        
    def stop(self):
        inputByteString = chr(1)
        self.serMain.write(inputByteString)
        self.serMain.readline()
        
    def getInfos(self):
        inputByteString = chr(2)
        self.serMain.write(inputByteString)
        returned = ""
        for i in range(0,11):
            r = self.serMain.read()
            returned += r.encode('hex')
        self.serMain.readline()
        
        l = []
        k = 0
        # while k < returned.length
        while k < 21:
            if k < 12:
#                print returned[k:k+4]
                r = int(returned[k:k+4],16)
                if r > 32767:
                    r -= 65536
                k += 4
            else:
#                print returned[k:k+2]
                r = int(returned[k:k+2],16)
                if r > 32767:
                    r -= 65536
                k += 2
            l.append(r)        
        return l
    
    def getColor(self):
        re = '00'
        while(re == '00'):
            self.serCouleur.write(chr(255))
            time.sleep(1)
            a = self.serCouleur.read()
            self.serCouleur.readline()
            re = a.encode('hex')
        if (re == '01'): return 'J'
        else: return 'V'
        
    def envoiColor(self, couleur):
        if (couleur == 'J'): self.serMain.write(chr(255))
        else: self.serMain.write(chr(253))
        self.serMain.readline()
        
    def getGachette(self):
        self.serMain.write(chr(254))
        time.sleep(0.5)
        a = self.serMain.read()
        self.serMain.readline()
        if (a.encode('hex') == '00'): return False
        else: return True 
        
        #############
        #Appels actionneurs gobelets
        
    def appelMonteeActionneurGobeletDevant(self):
        self.serMain.write(chr(3))
        time.sleep(0.25)
        self.serMain.readline()
        
    def appelMonteeActionneurGobeletDerriere(self):
        self.serMain.write(chr(5))
        time.sleep(0.25)
        self.serMain.readline()
        
    def appelDescenteActionneurGobeletDevant(self):
        self.serMain.write(chr(4))
        time.sleep(0.25)
        self.serMain.readline()
        
    def appelDescenteActionneurGobeletDerriere(self):
        self.serMain.write(chr(6))
        time.sleep(0.25)
        self.serMain.readline()

        #############
        #Appels actionneurs claps
        
    def appelMonteeClapGauche(self):
        self.serMain.write(chr(8))
        time.sleep(0.25)
        self.serMain.readline()
        time.sleep(1)
        
    def appelMonteeClapDroit(self):
        self.serMain.write(chr(10))
        time.sleep(0.25)
        self.serMain.readline()
        
    def appelDescenteClapGauche(self):
        self.serMain.write(chr(7))
        time.sleep(0.25)
        self.serMain.readline()
        
    def appelDescenteClapDroit(self):
        self.serMain.write(chr(9))
        time.sleep(0.25)
        self.serMain.readline()
        
        #############
        #Appels actionneurs cylindres
        #inverse devant derriere
        
        #montee derriere
    def appelMonteePinceDevant(self):
        self.serMain.write(chr(11))
        time.sleep(0.25)
        self.serMain.readline()
        
        #descente incontrollée à l'infini
    def appelMonteePinceDerriere(self):
        self.serMain.write(chr(13))
        time.sleep(0.25)
        self.serMain.readline()
        
        #descente derriere
    def appelDescentePinceDevant(self):
        self.serMain.write(chr(12))
        time.sleep(0.25)
        self.serMain.readline()
        
        #montee devant
    def appelDescentePinceDerriere(self):
        self.serMain.write(chr(14))
        time.sleep(0.25)
        self.serMain.readline()
        
    def appelSortiePinceDevant(self):
        self.serMain.write(chr(15))
        time.sleep(0.25)
        self.serMain.readline()
        
    def appelSortiePinceDerriere(self):
        self.serMain.write(chr(17))
        time.sleep(0.25)
        self.serMain.readline()
        
    def appelRetourPinceDevant(self):
        self.serMain.write(chr(16))
        time.sleep(0.25)
        self.serMain.readline()
        
    def appelRetourPinceDerriere(self):
        self.serMain.write(chr(18))
        time.sleep(0.25)
        self.serMain.readline()
    
    def appelFermeturePinceDevant(self):
        self.serMain.write(chr(19))
        time.sleep(0.25)
        self.serMain.readline()
        
    def appelFermeturePinceDerriere(self):
        self.serMain.write(chr(22))
        time.sleep(0.25)
        self.serMain.readline()
        
    def appelOuvertureInternePinceDevant(self):
        self.serMain.write(chr(20))
        time.sleep(0.25)
        self.serMain.readline()
        
    def appelOuvertureInternePinceDerriere(self):
        self.serMain.write(chr(23))
        time.sleep(0.25)
        self.serMain.readline()
        
    def appelOuvertureExternePinceDevant(self):
        self.serMain.write(chr(21))
        time.sleep(0.25)
        self.serMain.readline()
        
    def appelOuvertureExternePinceDerriere(self):
        self.serMain.write(chr(24))
        time.sleep(0.25)
        self.serMain.readline()
        
    ################
    ##capteurs remis à jour
        
    def envoiDistanceRemettre(self):
        #pour remettre la distance des capteurs à la valeur normale
        self.serCouleur.write(chr(200))
        time.sleep(0.25)
        self.serCouleur.readline()
        
    ################
    ##debug arduino (envoyé à arduino couleur pour affichage)
        
    def envoiCouleurReady(self):
        self.serCouleur.write(chr(2))
        time.sleep(0.25)
        self.serCouleur.readline()
        
    def envoiAllGreen(self):
        self.serCouleur.write(chr(3))
        time.sleep(0.25)
        self.serCouleur.readline()
        
    def envoiDepartZone(self):
        self.serCouleur.write(chr(4))
        time.sleep(0.25)
        self.serCouleur.readline()
        
    def envoiErreurArduino(self):
        self.serCouleur.write(chr(5))
        time.sleep(0.25)
        self.serCouleur.readline()
