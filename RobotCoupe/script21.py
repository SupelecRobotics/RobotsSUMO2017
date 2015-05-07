# -*- coding: utf-8 -*-


from Robot import Robot
import time

robot = Robot('/dev/ttyACM0','/dev/ttyACM1','/dev/ttyACM2')

#robot.bouge(200, 0)
print 'pré pouet'
robot.allerA(( 910, 850))
print 'pouet'
time.sleep(1)
#robot.bouge(100, 0)
print 'post pouet'

# robot.bouge(0, 900)
# robot.bouge(0, -900)



robot.goToCylindreLocal((910, 1170), True)

time.sleep(1)


robot.com.appelDescenteActionneurGobeletDevant()

