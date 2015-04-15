# -*- coding: utf-8 -*-
"""
Created on Wed Apr 08 22:03:07 2015

@author: Fabien
"""


from Robot import Robot
import time

robot = Robot('/dev/ttyACM0','/dev/ttyACM1','/dev/ttyACM2')

robot.allerAangle((int(200),int(550)), int(-900))
time.sleep(2)
#robot.allerAangle((int(600),int(1000)), int(1800))
#time.sleep(1)
robot.allerAangle((int(650),int(1100)), int(0))
time.sleep(2)
robot.allerAangle((int(1250),int(450)), int(1800))
time.sleep(2)
robot.allerAangle((int(2600),int(250)), int(1800))
time.sleep(2)
robot.allerAangle((int(2300),int(600)), int(0))
time.sleep(2)
robot.allerAangle((int(2600),int(1400)), int(1800))
time.sleep(2)
robot.allerAangle((int(2200),int(1400)), int(1800))
time.sleep(1)