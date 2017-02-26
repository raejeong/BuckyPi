import serial
import time
import random
import struct

ser = serial.Serial('/dev/ttyACM0',115200)
time.sleep(2)
while True:
	ser.write(struct.pack('>BBBB',255,255,255,0))
	print ser.readline()
	time.sleep(0.5)