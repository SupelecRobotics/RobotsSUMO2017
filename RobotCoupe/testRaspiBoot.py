import serial
import time

file = open('/home/pi/debugComArd.txt','w')
file.write('Debut')
try:
	sera = serial.Serial('/dev/ttyACM0', 115200)
except:
	file.write('Pb serial')

time.sleep(3)
sera.write(chr(250))
time.sleep(1)

a = sera.write()
file.write(a)

file.close()
