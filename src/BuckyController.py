maxVoltage = 13
minVoltage = 0
kP = [8, 1, 1]
kD = [0.2, 0, 0]
kT = [0.0225, 0.0225, 0.0225]
kE = [0.0198, 0.0198, 0.0198]
resistance = [0.8, 0.8, 0.8]
torque = [0, 0, 0]
xRef = [-0.18, 0, 0]
xError = [0, 0, 0]
xErrorOld = [0, 0, 0]
motorVoltage = [0, 0, 0]

def sign(x):
    if x > 0:
        return int(1)
    elif x < 0:
        return int(0)
    else:
        return int(0)

def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)

def controls(robotState, controlLoopPeriod):
	for i in range(0,2):
		xError[i] = xRef[i] - robotState[i+3]
		torque[i] = kP[i]*xError[i] + kD[i]*(xError[i]-xErrorOld[i])/controlLoopPeriod
		xErrorOld[i] = xError[i]
		motorVoltage[i] = (resistance[i]/kT[i])*torque[i] + kE[i]*robotState[i]
		motorVoltage[i] = max(min(maxVoltage, motorVoltage[i]), -maxVoltage)
	return motorVoltage

def getDirPWM(uInput):
	dirOutput = [0, 0, 0]
	PWMOutput = [0, 0, 0]

	for i in range(0,3):
		dirOutput[i] = sign(uInput[i])

	for i in range(0,3):
		PWMOutput[i] = int(translate(abs(uInput[i]),minVoltage,maxVoltage,0,254))
		if PWMOutput[i] < 30:
			PWMOutput[i] = 0

	return dirOutput, PWMOutput
