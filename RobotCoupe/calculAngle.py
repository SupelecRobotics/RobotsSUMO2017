# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 21:15:54 2015

@author: xubuntu
"""
import math

def xor(a, b)   :
    return ((a and (not b)) or ((not a) and b))
    

#print xor(True, False)
#print xor(False, False)

def nxor(a, b)  :
    return (not ((a and (not b)) or ((not a) and b)))
    
    
# nxor(True, False)
#print nxor(False, False)


def donneAlpha(orientationInitiale, sens, l, d1, d2, gobelet) :
#    orientationInitiale : bool qui vaut vrai si les slots à gauche sont pour les gobelets
#    sens : bool qui vaut true si l'objectif est devant le robot
#    l : int égal à la distance centre robot à centre gobelet
#    d1 : int égal à la distance sur une arête entre le centre du robot et le milieu du slot du gobelet
#    d2 : int idem pour le slot plot
#    gobelet : bool vrai si l'objectif est un gobelet, et faux si c'est un plot
    
    a = nxor(gobelet, orientationInitiale)
    
    if(xor(a, sens))    :
        signeAlpha = 1
    else :
        signeAlpha = -1
    
    if(a)  :
        d = d1
    else :
        d = d2
    
    alpha = signeAlpha*math.asin(float(d) / float(l))*360/(2*math.pi)
    
    return alpha
    
#print donneAlpha(True, True, 500, 20, 30, True)
    
def donneL(alpha, l, profSpot)	:
	Lprime = abs(l * math.cos(float(alpha)*2*math.pi/360))
	L = float(profSpot) / float(2) + Lprime - 10
	
	return L