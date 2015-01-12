# -*- coding: utf-8 -*-
"""
Created on Fri Jan 09 00:07:02 2015

@author: Fabien
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# Le Raspbery Pi demande une information à l'Arduino,
# puis il affiche la réponse à l'écran
 
import serial # bibliothèque permettant la communication série
import time # pour le délai d'attente entre les messages
 
ser = serial.Serial('/dev/ttyACM0', 9600)
time.sleep(4) #on attend un peu, pour que l'Arduino soit prêt.
d = 400             #distance : 2 byte max
d1 = d >> 8
d2 = d - d1 << 8
theta = 300         #theta : 2 byte max
t1 = theta >> 8
t2 = theta - t1 << 8
satVitesse = 120    #saturation vitesse : 1 byte max

inputByteString = chr(d) + chr(theta) + chr(satVitesse)
x = bytearray(b'128 132 139 2 0 0')
 
while True: # boucle répétée jusqu'à l'interruption du programme
#    ser.write('5')
    ser.write(inputByteString)
    print(ser.readline()) #on affiche la réponse
    
    ser.write(x)
    print(ser.readline())
    
    time.sleep(1) # on attend pendant 1 seconde 