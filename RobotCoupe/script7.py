# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 16:29:55 2015

@author: Fabien
"""


from Robot import Robot
import time

robot = Robot('/dev/ttyACM0','/dev/ttyACM1','/dev/ttyACM2')
robot.printPosition()
robot.allerA((350,450))
robot.printPosition()
time.sleep(2)
robot.printPosition()
