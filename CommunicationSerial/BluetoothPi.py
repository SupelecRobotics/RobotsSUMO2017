#! /usr/bin/python
#use sudo

import serial
import RPi.GPIO as GPIO
import time

pinEN = 18
#pinVCC = 16
pause = 1

BlueTSer = serial.Serial( "/dev/ttyAMA0", baudrate=38400,timeout = 5 )

GPIO.setmode(GPIO.BOARD)

GPIO.setup(pinEN, GPIO.OUT)
#GPIO.setup(pinVCC, GPIO.OUT)

#GPIO.output(pinVCC, True)
#time.sleep(pause)
GPIO.output(pinEN, True)
time.sleep(pause)
#GPIO.output(pinVCC, False)
#time.sleep(pause)

print "Configuration"
BlueTSer.write("AT\r\n")
time.sleep(pause)
BlueTSer.write("AT+ORGL\r\n")
print "ORGL sent"
time.sleep(pause)
BlueTSer.write("AT+RMAAD\r\n")
print "RMAAD sent"
time.sleep(pause)
BlueTSer.write("AT+PSWD=6666\r\n")
print "PSWD sent"
time.sleep(pause)
BlueTSer.write("AT+ROLE=0\r\n")
print "ROLE sent"
time.sleep(pause)
print "PinEN false"
GPIO.output(pinEN, False)
time.sleep(pause)
BlueTSer.write("AT\r\n")
BlueTSer.write("AT+RESET\r\n")
print "RESET sent"
time.sleep(15)

print "Reading Data Configuration"
sdata = BlueTSer.read()
time.sleep(1)
data_left = BlueTSer.inWaiting()
sdata += BlueTSer.read(data_left)
print "Configuration finished"
print sdata


a = None
while a == None:
    try:
        a = float( raw_input( "Please enter the first number: " ) )
    except:
        pass    # Ignore any errors that may occur and try again

b = None
while b == None:
    try:
        b = float( raw_input( "Please enter the second number: " ) )
    except:
        pass    # Ignore any errors that may occur and try again

BlueTSer.write( "{0} {1}".format( a, b ) )
print BlueTSer.readline()
