# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 10:45:59 2015

@author: Fabien
"""

from Robot import Robot
import time

robot = Robot('/dev/ttyACM0','/dev/ttyACM1','/dev/ttyACM2')

robot.com.appelMonteeGobeletDevant()
time.sleep(2)
robot.com.appelDescenteGobeletDevant()
robot.com.appelMonteeGobeletDerriere()
time.sleep(2)
robot.com.appelDesceneGobeletDerriere()

robot.com.appelDescenteClapDroit()
time.sleep(2)
robot.com.appelMonteeClapDroit()

robot.com.appelDescenteClapGauche()
time.sleep(2)
robot.com.appelMonteeClapGauche()