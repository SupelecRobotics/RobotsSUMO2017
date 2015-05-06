# -*- coding: utf-8 -*-


from Robot import Robot
import time

robot = Robot('/dev/ttyACM0','/dev/ttyACM1','/dev/ttyACM2')
##########################
#3 cylindres + 1 gobelet
#
#pos robot 
#pos cyl 870, 645
#pos cyl 1100, 230
#pos cyl 1300, 600
#pos gob 1500, 350
#
#3 cylindres
#
#cyl 850, 1800
#cyl 850, 1900
#cyl 90, 1800
#
#
#
#
#



robot.allerA(( 450, 450))

time.sleep(1)

# robot.bouge(0, 900)
# robot.bouge(0, -900)


robot.updatePosition()

robot.goToGobeletLocal((250, 250), True)



#1er plot


robot.goToCylindreLocal((90, 250), True)

time.sleep(3)



#plot 2

robot.goToCylindreLocal((90, 150), True)

time.sleep(3)

robot.bouge(0, -500)
robot.bouge(-500, 0)


robot.com.appelDescenteActionneurGobeletDevant()

