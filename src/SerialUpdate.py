import serial
import time
import struct

ser = serial.Serial('/dev/ttyACM0',115200)
time.sleep(2)

def update(dirc, pwm):
	ser.write(struct.pack('>BBBBBB',dirc[0],dirc[1],dirc[2],pwm[0],pwm[1],pwm[2]))
	stateString = ser.readline()
	stateString = stateString.strip().split(",")
	return list(map(float,stateString))