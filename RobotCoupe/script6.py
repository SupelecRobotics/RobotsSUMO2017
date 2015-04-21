# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 14:49:22 2015

@author: Fabien
"""

from Robot import Robot
import time

robot = Robot('/dev/ttyACM0','/dev/ttyACM1','/dev/ttyACM2')
robot.printPosition()
robot.bouge(200,0)
robot.printPosition()
time.sleep(2)
robot.printPosition()
#robot.bougeBest(0,100)
#robot.printPosition()
