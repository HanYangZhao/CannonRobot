import os
import RPi.GPIO as GPIO
import serial
import time

ser = serial.Serial('/dev/ttyAMA0',9600,timeout=1)

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

	pipein.close()
