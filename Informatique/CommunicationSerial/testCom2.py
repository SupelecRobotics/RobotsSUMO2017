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
d = 0x004F
theta = 0x00FF
satVitesse = 0x12

inputByteString = chr(d) + chr(theta) + chr(satVitesse)
x = bytearray(b'128 132 139 2 0 0')
 
while True: # boucle répétée jusqu'à l'interruption du programme
#    ser.write('5')
    ser.write(inputByteString)
    print(ser.readline()) #on affiche la réponse
    
    ser.write(x)
    print(ser.readline())
    
    time.sleep(1) # on attend pendant 1 seconde 
    
    #d : 2 byte
    #theta : 2 byte
    #saturation vitesse : 1 byte