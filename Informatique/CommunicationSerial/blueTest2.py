import serial
import time

ser = serial.Serial("/dev/ttyAMA0", 38400, timeout=3)

ser.write("AT")
time.sleep(1)
#print ser.read()
