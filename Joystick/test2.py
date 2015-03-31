# -*- coding: utf-8 -*-
"""
Created on Mon Feb 02 19:09:59 2015

@author: Fabien
"""
import pygame
import sys
import time
from pygame.locals import *

pygame.init()
pygame.joystick.init()

print pygame.joystick.get_count()
if (pygame.joystick.get_count() != 0):
    _joystick = pygame.joystick.Joystick(0)
    _joystick.init()
    print _joystick.get_init()
    print _joystick.get_id()
    print _joystick.get_name()
    print _joystick.get_numaxes()
    print _joystick.get_numballs()
    print _joystick.get_numbuttons()
    print _joystick.get_numhats()
    print _joystick.get_axis(0)
    
cond = True



while (cond):
    g_keys = pygame.event.get()

    for event in g_keys:  
        if (event==JOYAXISMOTION):
            for i in range(0, _joystick.get_numaxes()-1):
                print "axis"
                string = ""
                if (_joystick.get_axis(i)):
                    string += (str(i) + " : " + str(_joystick.get_axis(i)))
                print string
    time.sleep(1)