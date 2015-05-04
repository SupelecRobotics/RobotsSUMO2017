# -*- coding: utf-8 -*-


from Robot import Robot
from calculAngle import donneAlpha
from calculAngle import donneL
import time

robot = Robot('/dev/ttyACM0','/dev/ttyACM1','/dev/ttyACM2')

print 'pré pouet'
robot.allerAangle(( 910, 850), 900)
print 'pouet'
robot.allerA((910, 950))
print 'post pouet'

orientationInitiale = True
sens = True
l = 25
d1 = 10
d2 = 30
gobelet = True
theta = donneAlpha(orientationInitiale, bool(sens), int(l), d1, d2, gobelet)
profSpot = 7
L = donneL(theta, int(l), profSpot)
L = L * 10
theta = (int)robot.theta + theta * 10

print theta
robot.bouge(0,int(theta))
robot.bouge(int(L),0)
robot.com.appelMonteeActionneurGobeletDevant()
time.sleep(2)
robot.com.appelDescenteActionneurGobeletDevant()
