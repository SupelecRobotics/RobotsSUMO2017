# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 10:45:59 2015

@author: Fabien
"""

from Robot import Robot
import time

robot = Robot('/dev/ttyACM0','/dev/ttyACM1','/dev/ttyACM2')

robot.bouge(0,-170)
robot.bouge(200,0)
robot.com.appelMonteeActionneurGobeletDevant()
robot.bouge(100,0)
time.sleep(1)
robot.com.appelDescenteActionneurGobeletDevant()
robot.bouge(-200,0)
#robot.bouge(0,-900)
#robot.com.appelDescenteActionneurGobeletDerriere()
#time.sleep(3)
#robot.com.appelMonteeActionneurGobeletDerriere()

#robot.com.appelDescenteClapDroit()
#robot.bouge(0,500)
#robot.bouge(0,-500)
#robot.com.appelMonteeClapDroit()
#robot.com.appelMonteeClapDroit()

#robot.com.appelDescenteClapGauche()
#robot.bouge(0,500)
#robot.bouge(0,-500)
#robot.com.appelMonteeClapGauche()
