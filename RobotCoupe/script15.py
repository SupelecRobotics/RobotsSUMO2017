# -*- coding: utf-8 -*-


from Robot import Robot
from calculAngle import donneAlpha
from calculAngle import donneL
import time

robot = Robot('/dev/ttyACM0','/dev/ttyACM1','/dev/ttyACM2')

robot.allerAangle(( 500, 250), 1800)
print 'pouet'


orientationInitiale = True
sens = True
l = 250
d1 = 10
d2 = 30
gobelet = True
theta = donneAlpha(orientationInitiale, bool(sens), int(l), d1, d2, gobelet)
profSpot = 7
L = donneL(theta, int(l), profSpot)
L = L * 10
theta = theta * 10

print theta
robot.bouge(0,int(theta))
robot.bouge(int(L),0)
robot.com.appelMonteeActionneurGobeletDevant()
time.sleep(2)
robot.com.appelDescenteActionneurGobeletDevant()
