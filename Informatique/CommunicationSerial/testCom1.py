# -*- coding: utf-8 -*-
"""
Created on Thu Jan 08 21:42:11 2015

@author: Fabien
"""

import serial
ser = serial.Serial('/dev/ttyACM0', 9600)
while 1 :
    print(ser.readline()) 