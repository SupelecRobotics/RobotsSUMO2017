# -*- coding: utf-8 -*-



from Robot import Robot
from calculAngle import donneAlpha
import time

robot = Robot('/dev/ttyACM0','/dev/ttyACM1','/dev/ttyACM2')
while(True)	:
	robot.printPosition()
	orientationInitiale = True
	sens = raw_input('Enter sens : ')
	l = raw_input('Enter l : ')
	d1 = 10
	d2 = 30
	gobelet = True
	d = int(l) / 2
	theta = theta * 10
	print theta
	robot.bouge(0,int(theta))
	robot.bouge(int(d),0)
	robot.com.appelMonteeActionneurGobeletDevant()
	time.sleep(2)
	robot.com.appelDescenteActionneurGobeletDevant()
	
robot.printPosition()