# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 15:45:53 2015

@author: Fabien
"""

from Robot import Robot
import time

robot = Robot('/dev/ttyACM0','/dev/ttyACM1','/dev/ttyACM2')

robot.game()