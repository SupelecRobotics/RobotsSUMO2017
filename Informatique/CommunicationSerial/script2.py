# -*- coding: utf-8 -*-
"""
Created on Fri Mar 06 00:46:02 2015

@author: Fabien
"""

import time
import CommunicationSerial as com

com = com.CommunicationSerial('/dev/ttyACM0','/dev/ttyACM0')

com.envoiMoteurCapteur(100,0)
time.sleep(2)
com.getInfos()
