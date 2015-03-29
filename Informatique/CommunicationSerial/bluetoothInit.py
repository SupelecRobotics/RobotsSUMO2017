def bluetoothInit():
    pinEN = 18
     
    pause = 1
    BlueTSer = serial.Serial( "/dev/ttyAMA0", baudrate=38400,timeout = 5 )
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pinEN, GPIO.OUT)
     
     
    GPIO.output(pinEN, True)
    time.sleep(pause)
     
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
     
    BlueTSer.write("AT\r\n")
    BlueTSer.write("AT+RESET\r\n")
    print "RESET sent"
     
    print "PinEN false"
    GPIO.output(pinEN, False)
     
     
     
    print "Reading Data Configuration wait 10sec"
    time.sleep(10)
    data_left = BlueTSer.inWaiting()
    sdata += BlueTSer.read(data_left)
    print "Configuration finished"
    print sdata
