# -*- coding: utf-8 -*-
import time
from CommunicationSerial import CommunicationSerial as com

com = com('/dev/ttyACM0','/dev/ttyACM0')

com.envoiMoteurCapteur(-50,0)
com.envoiMoteurCapteur(0,0)
time.sleep(2)
returned = com.getInfos()
#print returned
print returned[:4]
print returned[4:8]
print returned[8:12]
print returned[12:14]
print returned[14:16]
print returned[16:18]
print returned[18:20]