#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
#Created on Thu Apr 16 15:45:53 2015

#@author: Fabien
"""

from Robot import Robot
import time
#import logging

file = open('exception.txt', 'w')
file.write('Start\n')

#time.sleep(5)
#logging.basicConfig(level=logging.DEBUG, filename='/tmp/myapp.log')
#try :
robot = Robot('/dev/ttyACM0','/dev/ttyACM1','/dev/ttyACM2')
#	robot.printPosition()
file.write('Robot On\n')
robot.game()
#except:
#	logging.exception('Error')
#	e = sys.exc_info()[0]
#	file = open('exception.txt','w')
	#file.write(e)
