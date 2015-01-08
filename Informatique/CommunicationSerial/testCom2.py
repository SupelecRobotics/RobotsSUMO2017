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
 
while True: # boucle répétée jusqu'à l'interruption du programme
    ser.write('5')
    print(ser.readline()) #on affiche la réponse
    time.sleep(1) # on attend pendant 1 seconde 