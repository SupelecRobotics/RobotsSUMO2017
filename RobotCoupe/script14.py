# -*- coding: utf-8 -*-



from Robot import Robot
from calculAngle import donneAlpha
import time

robot = Robot('/dev/ttyACM0','/dev/ttyACM1','/dev/ttyACM2')
while(True)	:
	robot.printPosition()
	orientationInitiale = True
	sens = True
	l = raw_input('Enter l : ')
	d1 = 100
	d2 = 300
	gobelet = True
	theta = donneAlpha(orientationInitiale, sens, l, d1, d2, gobelet)
	print theta
	robot.bouge(int(l/2),int(theta))
	
	time.sleep(2)
robot.printPosition()