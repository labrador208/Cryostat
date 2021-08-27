import time
import serial
#from serial.serialposix import Serial
#i=5
#print('starting', i ,'lol')


ser = serial.Serial(
	port='COM8',
	baudrate=9600,
	parity=serial.PARITY_ODD,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.SEVENBITS
)

print(ser.isOpen())
#ser.write(b"KRDG? 1\r\n")
#temp1=ser.readline().strip()
#tempfinal1=temp1.decode('ascii')
#print(tempfinal1)

#seconds=str(time())
#print(seconds)

#L=[time, " ",tempfinal1, "\n"]
#file1=open("MyFile.txt", "w")
#file1.writelines(L)
#file1.close()

#ser.write(b"KRDG? 1\r\n")
#temp1=ser.readline().strip()
#tempfinal1=temp1.decode('ascii')
#print(tempfinal1)

#ser.write(b"DATETIME?\r\n")
#time=ser.readline().strip()
#timefinal=time.decode('ascii')
#print(time)

L=["CTime Chan1 Chan2  Chan3  Chan4  Chan5  Chan6  Chan7  Chan8","\n"]
Y=["Seconds K K K K K K K K \n"]
titletime=(str(time.time()))
title=titletime+'.txt'
print(title)
file1=open(title, "w")
file1.writelines(L)
file1.writelines(Y)
file1.close()


#i=0
while 1:
	ser.write(b"KRDG? 1\r\n")
	temp1=ser.readline().strip()
	tempfinal1=temp1.decode('ascii')
	#print(tempfinal1)

	ser.write(b"KRDG? 2\r\n")
	temp2=ser.readline().strip()
	tempfinal2=temp2.decode('ascii')

	ser.write(b"KRDG? 3\r\n")
	temp3=ser.readline().strip()
	tempfinal3=temp3.decode('ascii')

	ser.write(b"KRDG? 4\r\n")
	temp4=ser.readline().strip()
	tempfinal4=temp4.decode('ascii')
	
	ser.write(b"KRDG? 5\r\n")
	temp5=ser.readline().strip()
	tempfinal5=temp5.decode('ascii')

	ser.write(b"KRDG? 6\r\n")
	temp6=ser.readline().strip()
	tempfinal6=temp6.decode('ascii')

	ser.write(b"KRDG? 7\r\n")
	temp7=ser.readline().strip()
	tempfinal7=temp7.decode('ascii')

	ser.write(b"KRDG? 8\r\n")
	temp8=ser.readline().strip()
	tempfinal8=temp8.decode('ascii')

	

	the_time=str(time.time())
	

	L=[the_time, " ",tempfinal1, " ", tempfinal2, " ", tempfinal3, " ", tempfinal4, " ", tempfinal5, " ", tempfinal6, " ", tempfinal7, " ", tempfinal8, "\n"]
	file1=open(title, "a")
	file1.writelines(L)
	file1.close()
	#i=i+1

print("Done")
