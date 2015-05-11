# -*- coding: utf-8 -*-


from Robot import Robot
import time

robot = Robot('/dev/ttyACM0','/dev/ttyACM1','/dev/ttyACM2')

# les deux cylindres en haut (P2 et P3)

robot.allerA((730, 1580))
robot.goToCylindreLocal((850, 1800), True)
robot.goToCylindreLocal((850, 1900), True)

# Gobelet G2 + dépose dans la zone de départ

robot.allerA((690, 1050))

robot.goToCylindreLocal((910, 1170), False)

# robot.bouge(0, -900)

# robot.allerAangle((600, 1000), 1800)
# robot.allerA((250, 1000))

# robot.com.appelDescenteActionneurGobeletDerriere()

# # Gobelet G1 + Cylindres P4 et P5

# robot.allerA(( 450, 450))
# robot.goToGobeletLocal((250, 250), True)

# #1er plot
# robot.goToCylindreLocal((90, 250), True)

# #plot 2
# robot.goToCylindreLocal((90, 150), True)

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


# 2 cylindres P7 P8 
robot.goToCylindreLocal((1100, 230), False)
robot.goToCylindreLocal((1300, 600), False)

# dépose des 4 cylindres
robot.allerA((1300, 310))
time.sleep(1)

# cylindre P6
robot.allerA((1040, 950))
robot.goToCylindreLocal((870, 645), False)


#poser gobelet + 3 cylindres + balle
robot.allerAangle((600, 1000), 0)
robot.allerA((450, 1000))

robot.com.appelDescenteActionneurGobeletDerriere()





# # poser 2 cylindres dans zone rouge
# # clap côté adverse

# # poser gobelet 1
# robot.allerA((2600, 600))

# # poser gobelet2
# robot.allerA((2600, 1400))

# # rentrer
# robot.allerAangle((600, 1000), 0)
# robot.allerA((250, 1000))




