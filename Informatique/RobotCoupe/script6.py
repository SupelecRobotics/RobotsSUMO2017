# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 14:49:22 2015

@author: Fabien
"""

from Robot import Robot

robot = Robot('/dev/ttyACM0','/dev/ttyACM0')
robot.printPosition()
robot.bougeBest((20,20))
robot.printPosition()
time.sleep(2)
robot.printPosition()
#robot.bougeBest(0,100)
#robot.printPosition()