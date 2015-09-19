#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time

# ===========================================================================
# Example Code
# ===========================================================================

# Initialise the PWM device using the default address
# bmp = PWM(0x40, debug=True)
pwm = PWM(0x40, debug=True)


XservoPin = 0
YservoPin = 1
XservoRight = 180 # Min pulse length out of 4096
XservoMid = 340
XservoLeft = 512  # Max pulse length out of 4096
YservoUp = 102
YservoMid = 320 
YservoDown = 440

def setServoPulse(channel, pulse):
  pulseLength = 1000000                   # 1,000,000 us per second
  pulseLength /= 50                       # 60 Hz
  print "%d us per period" % pulseLength
  pulseLength /= 4096                     # 12 bits of resolution
  print "%d us per bit" % pulseLength
  pulse *= 1000
  pulse /= pulseLength
  pwm.setPWM(channel, 0, pulse)

pwm.setPWMFreq(50)                        # Set frequency to 50 Hz
pwm.setPWM(XservoPin, 0, XservoMid)               # PWM 0 is the pan
pwm.setPWM(YservoPin, 0, YservoMid)               # PWM 1 is the tilt
time.sleep(1)
currentTilt = YservoMid
currentPan = XservoMid
#log = open("/home/pi/bin/servo/log", 'w')
while (True):

  pipein = open("/var/www/FIFO_piservo", 'r')
 # log.write("opened")
 # log.write("\n")
  line = pipein.readline()
  line_array = line.split(' ')
  if line_array[0] == "servo":
    print(line_array[1])
    print(line_array[2])
    if currentTilt + int(line_array[2]) < YservoDown  and currentTilt + int(line_array[2]) > YservoUp:
      if currentPan + int(line_array[1]) < XservoLeft and currentPan + int(line_array[1]) > XservoRight:
        currentTilt += int(line_array[2])
        currentPan += int(line_array[1])
        pwm.setPWM(YservoPin, 0, currentTilt)
        pwm.setPWM(XservoPin, 0, currentPan)

  elif line_array[0] == "led":
    p_led.createPiLight(int(line_array[1]),int(line_array[2]),int(line_array[3]))


  elif line_array[0] == "panning":
    print("panning")
    print(line_array[1])
    print(line_array[2])
    pwm.setPWM(XservoPin, 0, XservoLeft)               # PWM 0 is the pan
    time.sleep(1)
    currentPan = XservoLeft
    while (currentPan > 160):
      currentPan -= 1
      print(line_array[2])
      pwm.setPWM(XservoPin, 0, currentPan)
      time.sleep(.0225 * float(line_array[2]))
    time.sleep(1)
    pwm.setPWM(XservoPin, 0, XservoMid)
    currentPan = XservoMid
  
  elif line_array[0] == "tilting":
    pwm.setPWM(YservoPin, 0, YservoUp)
    time.sleep(1)
    currentTilt = YservoUp
    while (currentTilt < 440):
      currentTilt += 1
      pwm.setPWM(YservoPin, 0, currentTilt)
      time.sleep(.0225 * float(line_array[1]))
    time.sleep(1)
    pwm.setPWM(YservoPin, 0, YservoMid)
    currentTilt = YservoMid

  elif line_array[0] == "centering":
    print("centering")
    pwm.setPWM(YservoPin, 0, YservoMid)               # PWM 1 is the tilt
    time.sleep(0.3)
    pwm.setPWM(XservoPin, 0, XservoMid)               # PWM 0 is the pan
    currentPan = XservoMid
    currentTilt = YservoMid
    time.sleep(1)
  pipein.close()
