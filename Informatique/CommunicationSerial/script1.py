# -*- coding: utf-8 -*-
"""
Created on Thu Mar 05 22:28:05 2015

@author: Fabien
"""
import CommunicationSerial as com

com = com.CommunicationSerial('/dev/ttyACM0','/dev/ttyACM0')

com.envoiMoteurCapteur(40,0)
com.envoiMoteurCapteur(0,200)
com.envoiMoteurCapteur(40,0)
com.envoiMoteurCapteur(0,200)

com.envoiMoteurCapteur(0,-200)
com.envoiMoteurCapteur(-40,0)
com.envoiMoteurCapteur(0,-200)
com.envoiMoteurCapteur(-40,0)
