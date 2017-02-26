import mpu6050
import SerialUpdate
import BuckController
import time

direction = [0, 0, 0]
motorPWM = [0, 0, 0]
state = [0, 0, 0, 0, 0] # motorSpeed1, motorSpeed2, motorSpeed3, xAngle, yAngle
tPeriod = 0
tOld = 0
u = [0, 0, 0] # motor1Voltage, motor2Voltage, motor3Voltage

while  True:
	tPeriod = time.time() - tOld
	tOld = time.time()
	state = SerialUpdate.update(direction,motorPWM) + mpu6050.getAngle()
	u = BuckyController.controls(state, tPeriod)
	direction, motorPWM = BuckyController.getDirPWM(u)
	