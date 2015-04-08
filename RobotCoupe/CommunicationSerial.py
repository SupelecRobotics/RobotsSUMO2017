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
    
    def __init__(self, ser1, ser2) :
        self.serMoteurCapteur = serial.Serial(ser1, 9600)
        #self.serVideo = serial.Serial(ser2, 9600)
        time.sleep(3)
        
    def envoiMoteurCapteur(self, d=0, theta=0):
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
        self.serMoteurCapteur.write(inputByteString)
#        print("Envoi")
        self.serMoteurCapteur.readline()
#        print(self.serMoteurCapteur.readline())
        time.sleep(0.5)
        
    def envoiMoteurCapteurSat(self, d=0, theta=0, satVitesse=0):
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
        print satV
        
        inputByteString = chr(commande) + chr(d1) + chr(d2) + chr(t1) + chr(t2) + chr(satV)
        self.serMoteurCapteur.write(inputByteString)
#        print("Envoi")
        self.serMoteurCapteur.readline()
#        print(self.serMoteurCapteur.readline())
        time.sleep(0.5)
        
    def stop(self):
        inputByteString = chr(1)
        self.serMoteurCapteur.write(inputByteString)
#        print("Envoi")
        self.serMoteurCapteur.readline()
        time.sleep(0.5)
        
    def getInfos(self):
        inputByteString = chr(2)
        self.serMoteurCapteur.write(inputByteString)
#        print("Envoi")
        returned = ""
        for i in range(0,10):
            r = self.serMoteurCapteur.read()
            returned += r.encode('hex')
        re = self.serMoteurCapteur.readline()
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
