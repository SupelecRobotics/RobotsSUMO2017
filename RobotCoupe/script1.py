# -*- coding: utf-8 -*-
from CommunicationSerial import CommunicationSerial as com

com = com('/dev/ttyACM0','/dev/ttyACM0')

com.envoiMoteurCapteur(200,0)
com.envoiMoteurCapteur(0,900)
#com.envoiMoteurCapteur(100,0)
#com.envoiMoteurCapteur(0,200)

com.envoiMoteurCapteur(0,-900)
com.envoiMoteurCapteur(-200,0)
com.envoiMoteurCapteur(200,600)
#com.envoiMoteurCapteur(0,-200)
#com.envoiMoteurCapteur(-100,0)
