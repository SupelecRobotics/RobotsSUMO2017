# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 18:50:04 2015

@author: Fabien
"""

from Robot import Robot
import time

robot = Robot('/dev/ttyACM0','/dev/ttyACM1','/dev/ttyACM2')

robot.allerAangle((int(300),int(550)), int(-1170))
time.sleep(1)
robot.bouge(150,0)
#prend gobelet
#robot.com.appelActionneurMonteeGobeletDevant()
time.sleep(1)
robot.bouge(-150,0)
time.sleep(1)
robot.allerAangle((int(250),int(250)), int(-900))
robot.com.appelDescenteClapDroit()
robot.allerAangle((int(250),int(250)), int(0))
robot.allerAangle((int(850),int(250)), int(-900))
robot.allerAangle((int(850),int(250)), int(0))
robot.bouge(100,0)
robot.com.appelMonteeClapDroit()
# fait claps

robot.allerAangle((int(600),int(1000)), int(1800))
#robot.com.appelDescenteGobeletDevant()

#robot.allerAangle((int(600),int(1100)), int(1800))
#time.sleep(1)
#robot.bouge(0,310)
#time.sleep(1)
#robot.bouge(70,0)
##drop gobelet
#robot.com.appelDescenteGobeletDevant()
#time.sleep(1)
#robot.bouge(-280,0)
#time.sleep(1)
#robot.com.appelDescenteGobeletDerriere()
##prend gobelet
#
#attention, nécessité de tourner le robot
#robot.allerAangle((int(1200),int(450)), int(1800))
#time.sleep(1)
#robot.bouge(-150,0)
#time.sleep(1)
##prend gobelet
#
robot.allerAangle((int(2600),int(250)), int(1800))
robot.com.appelDescenteClapGauche()
robot.bouge(0,-500)
robot.bouge(0,500)
robot.bouge(200,0)
robot.com.appelMonteeClapGauche()
time.sleep(1)
##faire claps
#
#robot.allerAangle((int(2600),int(600)), int(0))
#time.sleep(1)
##drop gobelet
#
#robot.allerAangle((int(2700),int(1400)), int(1800))
#time.sleep(1)
##drop gobelet



##cote vert
#robot.allerAangle((int(2700),int(550)), int(-800))
#time.sleep(1)
#robot.bouge(150,0)
##prend gobelet
#robot.com.appelMonteeGobeletDerriere()
#time.sleep(1)
#robot.bouge(-150,0)
#time.sleep(1)
#robot.allerAangle((int(2750),int(250)), int(1150))
#robot.com.appelDescenteClapDroit()
#robot.allerAangle((int(2750),int(250)), int(0))
#robot.allerAangle((int(2600),int(250)), int(0))
#robot.allerAangle((int(2400),int(350)), int(0))
#robot.allerAangle((int(2200),int(250)), int(0))
#robot.allerAangle((int(2000),int(250)), int(0))
#robot.com.appelMonteeClapDroit()
#
#robot.allerAangle((int(2400),int(1000)), int(1800))
#robot.com.appelDescenteGobeletDerriere()

#robot.allerAangle((int(400),int(250)), int(1800))
#robot.com.appelDescenteClapGauche()
#robot.allerAangle((int(700),int(250)), int(1800))
#robot.com.appelMonteeClapGauche()
#time.sleep(1)
#faire claps