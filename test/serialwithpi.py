import os
import RPi.GPIO as GPIO
import serial
import time

GPIO.setmode(GPIO.BCM)
#GPIO.setup(17, GPIO.OUT)
#GPIO.setup(27, GPIO.OUT)
#GPIO.setup(27, GPIO.OUT)

while (True):

	ser = serial.Serial('/dev/ttyACM0', 9600, timeout=3)
	ser.open()
	ser.write('1')

time.sleep(1)