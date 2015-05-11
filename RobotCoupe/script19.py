# -*- coding: utf-8 -*-


from Robot import Robot
import time

robot = Robot('/dev/ttyACM0','/dev/ttyACM1','/dev/ttyACM2')

##passage coin inférieur gauche
#
#robot.allerA(( 450, 450))
#
#
#
#
#robot.goToGobeletLocal((250, 250), True)
#
#
#
##1er plot
#
#
#robot.goToCylindreLocal((90, 250), True)
#
#
#
#
#
##plot 2
#
#robot.goToCylindreLocal((90, 150), True)
#
#
#
#robot.com.appelDescenteActionneurGobeletDevant()

robot.com.appelMonteeActionneurGobeletDevant()
robot.com.appelDescenteActionneurGobeletDevant()

robot.allerA((2400, 450))

robot.allerA((600, 450))

robot.allerA((1000, 1000))
robot.allerA((1200, 1000))
robot.allerA((1800, 1000))