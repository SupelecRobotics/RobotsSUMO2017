# -*- coding: utf-8 -*-


from Robot import Robot
from CommunicationSerial import CommunicationSerial as com
import time

robot = Robot('/dev/ttyACM0','/dev/ttyACM1','/dev/ttyACM2')

#robot.bouge(200, 0)
print 'pré pouet'
robot.allerA(( 350, 220))
print 'pouet'
time.sleep(1)
#robot.bouge(100, 0)
print 'post pouet'

# robot.bouge(0, 900)
# robot.bouge(0, -900)



#robot.allerAangle((int(250),int(250)),-900)
robot.com.appelMonteeActionneurGobeletDevant()
# robot.com.appelDescenteClapDroit()
# robot.allerAangle((int(250),int(250)), 0)
# robot.com.appelMonteeClapDroit()

# robot.allerAangle((int(700),int(250)), 0)
# robot.com.appelDescenteClapDroit()
# robot.allerAangle((int(900),int(250)), 0)
# robot.com.appelMonteeClapDroit()

