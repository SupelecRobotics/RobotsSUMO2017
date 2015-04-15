# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 18:50:04 2015

@author: Fabien
"""

from Robot import Robot
import time

robot = Robot('/dev/ttyACM0','/dev/ttyACM1','/dev/ttyACM2')

robot.allerAangle((int(300),int(550)), int(-1000))
time.sleep(1)
robot.bouge(100,0)
#prend gobelet
time.sleep(1)
# fait claps

#robot.allerAangle((int(650),int(1100)), int(0))
#time.sleep(1)
#robot.bouge(50)
#robot.bouge(-100,0)
##drop gobelet
#robot.bouge(200,0)
#time.sleep(1)
##prend gobelet
#
#robot.allerAangle((int(1250),int(450)), int(1800))
#time.sleep(1)
#robot.bouge(100,0)
#time.sleep(1)
##prend gobelet
#
#robot.allerAangle((int(2600),int(250)), int(1800))
#time.sleep(1)
##faire claps
#
#robot.allerAangle((int(2600),int(600)), int(0))
#time.sleep(1)
##drop gobelet
#
#robot.allerAangle((int(2700),int(1400)), int(1800))
#time.sleep(1)
##drop gobelet
