# -*- coding: utf-8 -*-
"""
Created on Fri Mar 06 00:46:02 2015

@author: Fabien
"""

import time
from ..communication import CommunicationSerial as com

#run python -m Robot.scripts.script2 in /Informatique

com = com.CommunicationSerial('/dev/ttyACM0','/dev/ttyACM0')

com.envoiMoteurCapteur(100,0)
time.sleep(2)
com.getInfos()
