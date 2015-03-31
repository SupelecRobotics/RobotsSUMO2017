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

ser = serial.Serial('COM32', 9600)

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
            for i in range(0, 2):
                if (_joystick.get_axis(i)):
                    if (i==0): string += "x"
                    else: string+="y"
                    temp = int(_joystick.get_axis(i)*999)
                    if (temp >= 0):
                        string += "+"            
                    string += str(temp)
                    string += ";"
            print string
            ser.write(string)
        if (event.type == pygame.JOYBUTTONDOWN):
            if (_joystick.get_button(0)):
                ser.write("x+254;y+254;");
                print _joystick.get_button(0)
            if (_joystick.get_button(1)):
                ser.write("x-254;y-254;");
                print _joystick.get_button(1)
    time.sleep(0.2)