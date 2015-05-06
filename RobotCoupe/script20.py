# -*- coding: utf-8 -*-


from Robot import *
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



robot.allerA(( 700, 950))

time.sleep(1)

# robot.bouge(0, 900)
# robot.bouge(0, -900)


#1er plot

robot.goToCylindreLocal((870, 645), True)

time.sleep(3)

#plot 2

robot.updatePosition()

robot.allerA((900, 520))

robot.goToCylindreLocal((1100, 230), True)

time.sleep(3)

#plot 3

robot.updatePosition()

robot.allerA((1200, 260))

robot.goToCylindreLocal((1300, 600), True)

time.sleep(3)

#gobelet 

robot.updatePosition()

robot.allerA((1250, 300))

robot.goToGobeletLocal((1500, 350), True)

time.sleep(1)



robot.com.appelDescenteActionneurGobeletDevant()

