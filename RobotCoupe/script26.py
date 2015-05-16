#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
#Created on Today 8^)

#@author: Christian
"""
#### Test de pince !

from Robot import Robot
import time

robot = Robot('/dev/ttyACM0','/dev/ttyACM1','/dev/ttyACM2')

robot.updatePosition()

l = raw_input('Enter l : ')
sens = raw_input('Enter sens : ')

y = robot.y

if(bool(sens)) :
    x = robot.x + int(l)
else :
    x = robot.x - int(l)
    
point = (round(x), round(y))
    
robot.goToCylindreLocal(point, bool(sens))


