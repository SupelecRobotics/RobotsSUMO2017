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
    
    def __init__(self, ser1, ser2, ser3) :
        ser = serial.Serial(ser1, 115200)
#        serb = serial.Serial(ser2, 9600)
#        serc = serial.Serial(ser3, 9600)
        time.sleep(3)
        ser.write(chr(250))
#        print serb.write(chr(255))
#        print serc.write(chr(255))
        print "written"
        time.sleep(1)
        a = ser.read()
        ser.readline()
        #a = ser.readline()
        print a.encode('hex')
#        b = serb.read()
        #print b
#        c = serc.read()
        #print c
        print "read"
        #if (a == 0): self.serMain = serial.Serial(ser1, 9600)
        #elif (a == 1): self.serCouleur = serial.Serial(ser1, 9600)
        #else: self.serBluetooth = serial.Serial(ser1, 9600)
        #if (b == 0): self.serMain = serial.Serial(ser2, 9600)
        #elif (b == 1): self.serCouleur = serial.Serial(ser2, 9600)
        #else: self.serBluetooth = serial.Serial(ser2, 9600)
        #if (c == 0): self.serMain = serial.Serial(ser3, 9600)
        #elif (c == 1): self.serCouleur = serial.Serial(ser3, 9600)
        #else: self.serBluetooth = serial.Serial(ser3, 9600)
        self.serMain = serial.Serial(ser1, 9600)
        #self.serVideo = serial.Serial(ser2, 9600)
        time.sleep(3)
        
    def envoiMain(self, d=0, theta=0):
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
        self.serMain.write(inputByteString)
#        print("Envoi")
        self.serMain.readline()
#        print(self.serMoteurCapteur.readline())
        time.sleep(0.5)
        
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
#        print("Envoi")
        self.serMain.readline()
#        print(self.serMoteurCapteur.readline())
        time.sleep(0.5)
        
    def stop(self):
        inputByteString = chr(1)
        self.serMain.write(inputByteString)
#        print("Envoi")
        self.serMain.readline()
        time.sleep(0.5)
        
    def getInfos(self):
        inputByteString = chr(2)
        self.serMain.write(inputByteString)
#        print("Envoi")
        returned = ""
        for i in range(0,10):
            r = self.serMain.read()
            returned += r.encode('hex')
        re = self.serMain.readline()
#        return returnedString
        
        l = []
        k = 0
        # while k < returned.length
        while k < 19:
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
        time.sleep(0.5)
    
    def getColor(self):
        while(True):
        	self.serCouleur.write(chr(250))
		time.sleep(1)
        	a = self.serCouleur.read()
		self.serCouleur.readline()
		print a.encode('hex')
