# -*- coding: utf-8 -*-


from Robot import Robot
import time

robot = Robot('/dev/ttyACM0','/dev/ttyACM1','/dev/ttyACM2')

#passage coin inférieur gauche

robot.allerA(( 450, 450))




robot.goToGobeletLocal((250, 250), True)



#1er plot


robot.goToCylindreLocal((90, 250), True)





#plot 2

robot.goToCylindreLocal((90, 150), True)

time.sleep(3)

robot.bouge(0, -500)
robot.bouge(-500, 0)


robot.com.appelDescenteActionneurGobeletDevant()

