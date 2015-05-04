# -*- coding: utf-8 -*-


from Robot import Robot
from calculAngle import donneAlpha
from calculAngle import donneL
from util import *
import time

robot = Robot('/dev/ttyACM0','/dev/ttyACM1','/dev/ttyACM2')

# print 'pré pouet'
# robot.allerAangle(( 910, 850), 900)
# print 'pouet'
# time.sleep(1)
# #robot.bouge(100, 0)
# print 'post pouet'

# robot.bouge(0, 900)
# robot.bouge(0, -900)


# robot.updatePosition
orientationInitiale = True
sens = True
l = dist((robot.x, robot.y), (550, 1000))
d1 = 10
d2 = 30
gobelet = True
theta = donneAlpha(orientationInitiale, bool(sens), int(l), d1, d2, gobelet)
print theta
profSpot = 7
L = donneL(theta, int(l), profSpot)
L = L * 10
theta =  theta * 10 + int(robot.theta)


robot.bouge(0,int(theta))
time.sleep(1)
robot.bouge(int(L),0)
robot.com.appelMonteeActionneurGobeletDevant()
time.sleep(2)
robot.com.appelDescenteActionneurGobeletDevant()
