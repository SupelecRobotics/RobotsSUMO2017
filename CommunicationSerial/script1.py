# -*- coding: utf-8 -*-
"""
Created on Thu Mar 05 22:28:05 2015

@author: Fabien
"""
from Robot import CommunicationSerial

import CommunicationSerial as com

com = com.CommunicationSerial('/dev/ttyACM0','/dev/ttyACM0')

com.envoiMoteurCapteur(200,0)
com.envoiMoteurCapteur(0,900)
#com.envoiMoteurCapteur(100,0)
#com.envoiMoteurCapteur(0,200)

com.envoiMoteurCapteur(0,-900)
com.envoiMoteurCapteur(-200,0)
com.envoiMoteurCapteur(200,600)
#com.envoiMoteurCapteur(0,-200)
#com.envoiMoteurCapteur(-100,0)
