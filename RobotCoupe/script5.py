# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 19:47:24 2015

@author: Fabien
"""

from Robot import Robot

#print "a"
robot = Robot('/dev/ttyACM0','/dev/ttyACM1','/dev/ttyACM2')
#print "Robot created"
robot.printPosition()
#print "got position"
robot.bouge(100,0)
#print "moved"
robot.printPosition()
robot.bouge(0,100)
robot.printPosition()
