import serial
import time

ser = serial.Serial()
ser.baudrate = 115200
ser.port = 2
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
        y = y.replace(" ","")
        y = y.replace("\r\n","")
        y = y.replace("\n","")
        f_write = open("dynamic\\"+x+".txt","a").write(localtime[3]+"-"+str(y)+"\n")
    else:
        print data_raw