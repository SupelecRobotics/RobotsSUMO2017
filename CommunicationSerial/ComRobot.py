# -*- coding: utf-8 -*-
"""
Created on Thu Mar 05 21:36:47 2015

@author: Fabien
"""

import serial # bibliothèque permettant la communication série
import time # pour le délai d'attente entre les messages
 
serMoteurCapteur = serial.Serial('/dev/ttyACM0', 9600)
time.sleep(3)

def envoi(commande, d=0, theta=0):
    if (d<0):
       d = -d + 32768
    d1 = d >> 8
    d2 = d - (d1 << 8)
    if (theta<0): 
       theta = -theta + 32768
    t1 = theta >> 8
    t2 = theta - (t1 << 8)
    satVitesse = 200    #saturation vitesse : 1 byte max
    
    inputByteString = chr(commande) + chr(d1) + chr(d2) + chr(t1) + chr(t2) + chr(satVitesse)
    print serMoteurCapteur.write(inputByteString)
    print("Envoi Byte String")
    print(serMoteurCapteur.readline())
    time.sleep(0.5)
    
#envoi(1) #stop
#envoi(2) #infos
#envoi(0, 100, 0)
envoi(0, 0, 300)
#envoi(0, 100, 0)
#envoi(0, 0, 300)
#envoi(0 , -100, 0)
envoi(0, 0, -300)
envoi(1)
