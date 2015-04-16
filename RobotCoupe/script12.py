# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 10:45:59 2015

@author: Fabien
"""

from Robot import Robot
import time

robot = Robot('/dev/ttyACM0','/dev/ttyACM1','/dev/ttyACM2')

robot.com.appelMonteeActionneurGobeletDevant()
time.sleep(3)
robot.com.appelDescenteActionneurGobeletDevant()
robot.com.appelMonteeActionneurGobeletDerriere()
time.sleep(3)
robot.com.appelDescenteActionneurGobeletDerriere()
time.sleep(1)

robot.com.appelDescenteClapDroit()
time.sleep(1)
robot.com.appelMonteeClapDroit()
time.sleep(1)

robot.com.appelDescenteClapGauche()
time.sleep(1)
robot.com.appelMonteeClapGauche()
time.sleep(1)