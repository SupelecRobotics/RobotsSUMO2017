# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 18:50:04 2015

@author: Fabien
"""

from Robot import Robot
import time

robot = Robot('/dev/ttyACM0','/dev/ttyACM1','/dev/ttyACM2')

robot.allerAangle((int(220),int(550)), int(-900))
time.sleep(2)
robot.bouge(100,0)