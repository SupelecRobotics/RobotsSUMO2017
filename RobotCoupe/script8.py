# -*- coding: utf-8 -*-
"""
Created on Wed Apr 01 22:35:16 2015

@author: Fabien
"""

from Robot import Robot
import time

robot = Robot('/dev/ttyACM0','/dev/ttyACM0')

robot.printPosition()
while (True):
    d = raw_input('Enter a distance: ')
    theta = raw_input('Enter an angle: ')
    robot.bouge(0,theta)
    robot.bouge(d,0)
    time.sleep(1)