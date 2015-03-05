# -*- coding: utf-8 -*-
"""
Created on Fri Mar 06 00:46:02 2015

@author: Fabien
"""

import CommunicationSerial

com = CommunicationSerial('/dev/ttyACM0','/dev/ttyACM0')

com.getInfos(2)