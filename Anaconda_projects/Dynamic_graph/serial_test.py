import serial
import time

ser = serial.Serial()
ser.baudrate = 115200
ser.port = 3
ser.open()
while True:
    data_raw = ser.readline()
    if(data_raw == "\r\n"):
        print "empty line"
    elif "Dynamic" in data_raw:
            print "dyn raw"
    elif ":" in data_raw:
        print data_raw
        x,y = data_raw.split(':')
        localtime = time.asctime(time.localtime(time.time()))
        localtime = localtime.split(' ')
        y.replace(" ","")
        y.replace("\r","")
        y.replace("\n","")
        f_write = open("dynamic\\"+x+".txt","a").write(localtime[3]+","+str(y))
    else:
        print data_raw