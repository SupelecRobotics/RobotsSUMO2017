# -*- coding: utf-8 -*-
import time
from CommunicationSerial import CommunicationSerial as com

com = com('/dev/ttyACM0','/dev/ttyACM0')

com.envoiMoteurCapteur(100,0)
time.sleep(2)
returned = com.getInfos()