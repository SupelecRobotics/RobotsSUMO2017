# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 14:49:22 2015

@author: Fabien
"""

from Robot import Robot
import time

robot = Robot('/dev/ttyACM0','/dev/ttyACM0')
robot.printPosition()
robot.bougeDroit((20,0))
robot.printPosition()
time.sleep(2)
robot.printPosition()
#robot.bougeBest(0,100)
#robot.printPosition()