
from Robot import Robot
import time

robot = Robot('/dev/ttyACM0','/dev/ttyACM1','/dev/ttyACM2')



while (True):
    robot.printPosition()
    #    d = raw_input('Enter a distance: ')
    #    theta = raw_input('Enter an angle: ')
    #    robot.bouge(0,int(theta))
    #    robot.bouge(int(d),0)
    x = raw_input('Enter x : ')
    y = raw_input('Enter y : ')
    theta = raw_input('Enter theta : ')
    robot.allerAangle((int(x),int(y)), int(theta))
    time.sleep(1)

while(True):
    print 'pouet'

    print 'pouet'

    for i in range(0, 1):
        pouet = 20

    if(True):
        print 'true'
    else :
        pouet = 1



	
