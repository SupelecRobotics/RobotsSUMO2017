# -*- coding: utf-8 -*-


from Robot import Robot
import time

robot = Robot('/dev/ttyACM0','/dev/ttyACM1','/dev/ttyACM2')

# les deux cylindres en haut (P12 et P13)

robot.allerA((2270, 1580))
robot.goToCylindreLocal((2150, 1800), False)
robot.goToCylindreLocal((2150, 1900), False)

# Gobelet G2 + dépose dans la zone de départ

robot.allerA((2310, 1050))

robot.goToCylindreLocal((2090, 1170), True)


# Gobelet G + Cylindres 164 et P15

robot.allerA(( 2550, 450))
robot.goToGobeletLocal((2750, 250), False)

#1er plot
robot.goToCylindreLocal((2910, 250), False)

#plot 2
robot.goToCylindreLocal((2910, 150), False)

#claps
robot.allerAangle((int(2750),int(230)),900)
robot.com.appelMonteeActionneurGobeletDerriere()
robot.com.appelDescenteClapGauche()
robot.allerAangle((int(2750),int(230)), 1800)
robot.com.appelMonteeClapGauche()

robot.allerAangle((int(2300),int(230)), 1800)
robot.com.appelDescenteClapGauche()
#robot.allerAangle((int(900),int(230)), 0)
robot.bouge(int(2800),1800)
robot.com.appelMonteeClapGauche()


# 2 cylindres P7 P8 
robot.goToCylindreLocal((1900, 230), True)
robot.goToCylindreLocal((1700, 600), True)

# dépose des 4 cylindres
robot.allerA((1700, 310))
time.sleep(1)

# cylindre P6
robot.allerA((1960, 950))
robot.goToCylindreLocal((2130, 645), True)


#poser gobelet + 3 cylindres + balle
robot.allerAangle((2400, 1000), 1800)
robot.allerA((2550, 1000))

robot.com.appelDescenteActionneurGobeletDevant()





# # poser 2 cylindres dans zone rouge
# # clap côté adverse

# # poser gobelet 1
# robot.allerA((2600, 600))

# # poser gobelet2
# robot.allerA((2600, 1400))

# # rentrer
# robot.allerAangle((600, 1000), 0)
# robot.allerA((250, 1000))




