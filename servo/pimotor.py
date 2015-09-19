import os
import RPi.GPIO as GPIO
import serial
import time
from Adafruit_PWM_Servo_Driver import PWM

reloadServo = 2 
ser = serial.Serial('/dev/ttyAMA0',9600,timeout=1)
time.sleep(2)
pwm = PWM(0x40, debug=True)
pwm.setPWMFreq(50)
rServoOff = 220
rServoOn  = 510 
pwm.setPWM(reloadServo,0,rServoOff)
while(True):
	pipein = open("/var/www/FIFO_pimotor", 'r')
	line = pipein.readline()
	if line == "forward":
		ser.write('1')
	elif line == "backwards":
		ser.write('2')
	elif line == "right":
		ser.write('3')
	elif line == "left":
		ser.write('4')
	elif line == "stop":
		ser.write('0')
	elif line == "fire":
		ser.write('5')
	elif line == "reload":
		pwm.setPWM(reloadServo,0,rServoOn)
		time.sleep(0.4)
		pwm.setPWM(reloadServo,0,rServoOff)

	pipein.close()
