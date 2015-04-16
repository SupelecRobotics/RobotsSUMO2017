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
        ser = serial.Serial(ser1, 115200, timeout = 4)
        serb = serial.Serial(ser2, 115200, timeout = 4)
#        serc = serial.Serial(ser3, 57600)
        time.sleep(3)
        ser.write(chr(250))
        serb.write(chr(250))
#        print serc.write(chr(255))
#        print "written"
        time.sleep(1)
        a = ser.read()
        ser.readline()
        print a.encode('hex')
        time.sleep(1)
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
#        time.sleep(0.3)
        
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
#        time.sleep(0.3)
        
    def stop(self):
        inputByteString = chr(1)
        self.serMain.write(inputByteString)
#        print("Envoi")
        self.serMain.readline()
#        time.sleep(0.5)
        
    def getInfos(self):
        inputByteString = chr(2)
        self.serMain.write(inputByteString)
        print("Envoi")
        returned = ""
        for i in range(0,10):
            r = self.serMain.read()
            returned += r.encode('hex')
        self.serMain.readline()
        print("Get")
        
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
#        time.sleep(0.5)
    
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
#        self.serMain.write(chr(255))
#        time.sleep(1)
#        self.serMain.readline()
        if (couleur == 'J'): self.serMain.write(chr(255))
        else: self.serMain.write(chr(253))
        self.serMain.readline()
        
    def getGachette(self):
        self.serMain.write(chr(254))
        time.sleep(1)
        a = self.serMain.read()
        self.serMain.readline()
        if (a.encode('hex') == '00'): return False
        else: return True 
        
    def appelMonteeActionneurGobeletDevant(self):
        self.serMain.write(chr(3))
        time.sleep(1)
        self.serMain.readline()
        
    def appelMonteeActionneurGobeletDerriere(self):
        self.serMain.write(chr(5))
        time.sleep(1)
        self.serMain.readline()
        
    def appelDescenteActionneurGobeletDevant(self):
        self.serMain.write(chr(4))
        time.sleep(1)
        self.serMain.readline()
        
    def appelDescenteActionneurGobeletDerriere(self):
        self.serMain.write(chr(6))
        time.sleep(1)
        self.serMain.readline()
        
    def appelMonteeClapGauche(self):
        self.serMain.write(chr(7))
        time.sleep(1)
        self.serMain.readline()
        
    def appelMonteeClapDroit(self):
        self.serMain.write(chr(9))
        time.sleep(1)
        self.serMain.readline()
        
    def appelDescenteClapGauche(self):
        self.serMain.write(chr(8))
        time.sleep(1)
        self.serMain.readline()
        
    def appelDescenteClapDroit(self):
        self.serMain.write(chr(10))
        time.sleep(1)
        self.serMain.readline()
        
      
