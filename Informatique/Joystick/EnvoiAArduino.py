# -*- coding: utf-8 -*-
"""
Created on Thu Feb 05 22:42:02 2015

@author: Fabien
"""
import serial
import pygame
import sys
import time
from pygame.locals import *

#ser = serial.Serial('/dev/tty.usbserial', 9600)

pygame.init()
pygame.joystick.init()

if (pygame.joystick.get_count() == 0):
    print "No Joystick connected. Restart the app."
else:
    _joystick = pygame.joystick.Joystick(0)
    _joystick.init()
    
cond = True

while (cond):
    g_keys = pygame.event.get()

    for event in g_keys:  
        if (event.type == pygame.JOYAXISMOTION):
            string = ""
            for i in range(0, _joystick.get_numaxes()-1):
                if (_joystick.get_axis(i)):
                    string += ";"
                    temp = int(_joystick.get_axis(i)*999)
                    if (temp >= 0):
                        string += "+"
                    string += str(temp)
            print string
            #ser.write(string)
    time.sleep(2)