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
        try:
		ser = serial.Serial(ser1, 115200)
        except serial.SerialException:
            print "No connection to the first device could be established"
        try:
		serb = serial.Serial(ser2, 115200)
        except serial.SerialException:
            print "No connection to the second device could be established"
        
#        serc = serial.Serial(ser3, 57600)
        time.sleep(3)
        ser.write(chr(250))
        serb.write(chr(250))
#        print serc.write(chr(255))
        time.sleep(1)
        a = ser.read()
        ser.readline()
        print a.encode('hex')
#        time.sleep(1)
        b = serb.read()
        serb.readline()
        print b.encode('hex')
#        c = serc.read()
        #print c
        print "read"
        if (a.encode('hex') == '00'): self.serMain = serial.Serial(ser1, 115200)
        elif (a.encode('hex') == '01'): self.serCouleur = serial.Serial(ser1, 115200)
        else: self.serBluetooth = serial.Serial(ser1, 115200)
        if (b.encode('hex') == '00'): self.serMain = serial.Serial(ser2, 115200)
        elif (b.encode('hex') == '01'): self.serCouleur = serial.Serial(ser2, 115200)
        else: self.serBluetooth = serial.Serial(ser2, 115200)
        #if (c == 0): self.serMain = serial.Serial(ser3, 9600)
        #elif (c == 1): self.serCouleur = serial.Serial(ser3, 9600)
        #else: self.serBluetooth = serial.Serial(ser3, 9600)
        #self.serMain = serial.Serial(ser1, 9600)
        time.sleep(2)
        
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
        self.serMain.write(inputByteString)
        if (self.serMain.read().encode('hex') == '02'):
            return False
        self.serMain.readline()
        print "reçu"
        return True
        
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
        
    def appelMonteeActionneurCylindreDevant(self):
        self.serMain.write(chr(11))
        time.sleep(0.25)
        self.serMain.readline()
        
    def appelMonteeActionneurCylindreDerriere(self):
        self.serMain.write(chr(13))
        time.sleep(0.25)
        self.serMain.readline()
        
    def appelDescenteActionneurCylindreDevant(self):
        self.serMain.write(chr(12))
        time.sleep(0.25)
        self.serMain.readline()
        
    def appelDescenteActionneurCylindreDerriere(self):
        self.serMain.write(chr(14))
        time.sleep(0.25)
        self.serMain.readline()
        
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
