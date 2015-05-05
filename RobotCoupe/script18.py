# -*- coding: utf-8 -*-


from Robot import Robot
from calculAngle import donneAlpha
from calculAngle import donneL
from util import *
import time

robot = Robot('/dev/ttyACM0','/dev/ttyACM1','/dev/ttyACM2')

#robot.bouge(200, 0)
print 'pré pouet'
robot.allerA(( 450, 450))
print 'pouet'
#time.sleep(1)
#robot.bouge(100, 0)
print 'post pouet'

# robot.bouge(0, 900)
# robot.bouge(0, -900)


robot.updatePosition()

(x0, y0) = (robot.x,robot.y)
(x, y) = (250, 250)


delta = - robot.theta + angle((1, 0), (x - x0, y - y0))*1800/math.pi

robot.bouge(0, int(delta))
robot.updatePosition()

orientationInitiale = True
sens = True
robot.printPosition()
l = int(dist((robot.x, robot.y), (250, 250))) / 10
d1 = 10
d2 = 8.5
gobelet = True
theta = donneAlpha(orientationInitiale, bool(sens), int(l), d1, d2, gobelet)
print theta
profSpot = 7
L = donneL(theta, int(l), profSpot)
L = L * 10 + 60
theta =  theta * 10


robot.bouge(0,int(theta))
#time.sleep(1)
robot.bouge(int(L),0)
time.sleep(0.5)
robot.com.appelMonteeActionneurGobeletDevant()
#time.sleep(1)
robot.updatePosition()

#1er plot

(x0, y0) = (robot.x,robot.y)
(x, y) = (90, 250)


delta = - robot.theta + angle((1, 0), (x - x0, y - y0))*1800/math.pi

robot.bouge(0, int(delta))
robot.updatePosition()

orientationInitiale = True
sens = True
robot.printPosition()
l = int(dist((robot.x, robot.y), (90, 250))) / 10
d1 = 10
d2 = 8.5
gobelet = False
theta = donneAlpha(orientationInitiale, bool(sens), int(l), d1, d2, gobelet)
print theta
profSpot = 7
L = donneL(theta, int(l), profSpot)
L = L * 10 + 60
theta =  theta * 10


robot.bouge(0,int(theta))
#time.sleep(1)
robot.bouge(int(L),0)
time.sleep(3)

robot.updatePosition()

#plot 2


(x0, y0) = (robot.x,robot.y)
(x, y) = (90, 150)


delta = - robot.theta + angle((1, 0), (x - x0, y - y0))*1800/math.pi

robot.bouge(0, int(delta))
robot.updatePosition()

orientationInitiale = True
sens = True
robot.printPosition()
l = int(dist((robot.x, robot.y), (90, 150))) / 10
d1 = 10
d2 = 8.5
gobelet = False
theta = donneAlpha(orientationInitiale, bool(sens), int(l), d1, d2, gobelet)
print theta
profSpot = 7
L = donneL(theta, int(l), profSpot)
L = L * 10 + 60
theta =  theta * 10


robot.bouge(0,int(theta))
#time.sleep(1)
robot.bouge(int(L),0)
#time.sleep(3)

robot.bouge(0, -500)
robot.bouge(-500, 0)


robot.com.appelDescenteActionneurGobeletDevant()

