# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 19:47:24 2015

@author: Fabien
"""

from Robot import Robot

robot = Robot('/dev/ttyACM0','/dev/ttyACM0')
robot.printPosition()
robot.bouge(100,0)
robot.printPosition()
robot.bouge(0,100)
robot.printPosition()