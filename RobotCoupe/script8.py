# -*- coding: utf-8 -*-
"""
Created on Wed Apr 01 22:35:16 2015

@author: Fabien
"""

from Robot import Robot
import time

robot = Robot('/dev/ttyACM0','/dev/ttyACM0')


while (True):
    robot.printPosition()
#    d = raw_input('Enter a distance: ')
#    theta = raw_input('Enter an angle: ')
#    robot.bouge(0,int(theta))
#    robot.bouge(int(d),0)
    x = raw_input('Enter x : ')
    y = raw_input('Enter y : ')
    robot.bougeToPoint((x,y))
    time.sleep(1)