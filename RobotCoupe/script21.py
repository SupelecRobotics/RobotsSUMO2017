# -*- coding: utf-8 -*-


from Robot import Robot
import time

robot = Robot('/dev/ttyACM0','/dev/ttyACM1','/dev/ttyACM2')

#3 cylindres + gobelet
robot.allerA((700, 950))
robot.goToCylindreLocal((870, 645), False)
robot.allerA((900, 520))
robot.goToCylindreLocal((1100, 230), False)
robot.goToCylindreLocal((1300, 600), False)

robot.allerA((1250, 400))
robot.goToGobeletLocal((1500, 350), False)


#gobelet

robot.allerA((910, 850))
robot.goToGobeletLocal((910, 1170), True)

#poser gobelet + 3 cylindres + balle
robot.allerAangle((600, 1000), 0)
robot.allerA((450, 1000))

#2 cylindres + gobelet

#robot.allerA((450, 450))
#robot.goToGobeletLocal((250, 250), True)
#robot.goToCylindreLocal((90, 250), True)
#robot.goToCylindreLocal((90, 150), True)

#claps
robot.allerAangle((int(250),int(230)),-900)
robot.com.appelMonteeActionneurGobeletDevant()
robot.com.appelDescenteClapDroit()
robot.allerAangle((int(250),int(230)), 0)
robot.com.appelMonteeClapDroit()

robot.allerAangle((int(700),int(230)), 0)
robot.com.appelDescenteClapDroit()
#robot.allerAangle((int(900),int(230)), 0)
robot.bouge(int(200),0)
robot.com.appelMonteeClapDroit()

#chercher cylindres près des distributeurs?? (temps tros short)

#poser 2 cylindres dans zone rouge
#clap côté adverse

#poser gobelet 1
robot.allerA((2600, 600))

#poser gobelet2
robot.allerA((2600, 1400))

#rentrer
robot.allerAangle((600, 1000), 0)
robot.allerA((250, 1000))




