# -*- coding: utf-8 -*-


from Robot import Robot
import time

robot = Robot('/dev/ttyACM0','/dev/ttyACM1','/dev/ttyACM2')

robot.allerA(( 910, 850))
robot.goToCylindreLocal((910, 1170), True)

time.sleep(1)

robot.allerA(( 450, 450))
robot.goToGobeletLocal((250, 250), True)
robot.goToCylindreLocal((90, 250), True)
robot.goToCylindreLocal((90, 150), True)


robot.allerA(( 700, 950))
robot.goToCylindreLocal((870, 645), False)
#robot.allerA((900, 520))
robot.goToCylindreLocal((1100, 230), False)
robot.goToCylindreLocal((1300, 600), False)

robot.allerA((1250, 400))
robot.goToGobeletLocal((1500, 350), False)


robot.allerAangle((600, 1000), 0)
robot.allerA((250, 1000))

