# -*- coding: utf-8 -*-


from Robot import Robot
from CommunicationSerial import CommunicationSerial as com
import time

robot = Robot('/dev/ttyACM0','/dev/ttyACM1','/dev/ttyACM2')

sens = False
gobelet = True
point = (910, 850)

robot.allerA(point)
#robot.allerAangle(point, 0)
if(gobelet)  :
    robot.goToGobeletLocal((910, 1170), sens)
else :
    robot.goToCylindreLocal((910, 1170), sens)


time.sleep(1)

if(gobelet and sens)  :
    robot.com.appelDescenteActionneurGobeletDevant()
elif(gobelet and (not sens)) :
    robot.com.appelDescenteActionneurGobeletDerriere()
elif((not gobelet) and sens) :
    robot.com.appelDescenteActionneurCylindreDevant()
else :
    robot.com.appelDescenteActionneurCylindreDerriere()

robot.allerA(point)
robot.allerAangle((600, 1000), 0)
robot.allerA((250, 1000))
