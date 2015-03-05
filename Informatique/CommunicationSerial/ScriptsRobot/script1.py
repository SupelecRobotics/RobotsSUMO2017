# -*- coding: utf-8 -*-
"""
Created on Thu Mar 05 22:28:05 2015

@author: Fabien
"""
from ... import CommunicationSerial

com = CommunicationSerial('/dev/ttyACM0','/dev/ttyACM0')

com.envoiMoteurCapteur(0,100,0)
com.envoiMoteurCapteur(0,0,450)
com.envoiMoteurCapteur(0,100,0)
com.envoiMoteurCapteur(0,0,450)

com.envoiMoteurCapteur(0,0,-450)
com.envoiMoteurCapteur(0,-100,0)
com.envoiMoteurCapteur(0,0,-450)
com.envoiMoteurCapteur(0,-100,0)
