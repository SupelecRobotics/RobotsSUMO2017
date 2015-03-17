# -*- coding: utf-8 -*-
import time
from CommunicationSerial import CommunicationSerial as com

com = com('/dev/ttyACM0','/dev/ttyACM0')

com.envoiMoteurCapteur(-50,0)
com.envoiMoteurCapteur(0,0)
time.sleep(2)
returned = com.getInfos()
print returned
print returned[:2]
print returned[2:4]
print returned[4:6]
print returned[6:7]
print returned[7:8]
print returned[8:9]
print returned[9:10]