# -*- coding: utf-8 -*-
import time

from Robot import Robot

robot = Robot('/dev/ttyACM0','/dev/ttyACM1','/dev/ttyACM2')


while (True):
    robot.printPosition()
#    d = raw_input('Enter a distance: ')
#    theta = raw_input('Enter an angle: ')
#    robot.bouge(0,int(theta))
#    robot.bouge(int(d),0)
    d = raw_input('Enter d : ')
    theta = raw_input('Enter theta : ')
    robot.bouge(int(d),int(theta))
    time.sleep(1)