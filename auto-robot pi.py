""" this program will use the GPIO pins to run the motors of the robot pi,
and the ultrasonic sensor to sense distance. this will run and make the robot
automatic.
created by Andy Whiteman, 3-14-2018
"""

#import all libraries needed
import RPi.GPIO as GPIO
import time

#set GPIO library mode and warnings
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#sets variables used for the ultrasonic sensor and for controlling motor speed
pT = 17
pE = 18
HowNear = 15.0
frequency = 20
dutyCycleA = 50
dutyCycleB = 37

#sets up GPIO pins for use in program
GPIO.setup(pT, GPIO.OUT)
GPIO.setup(pE, GPIO.IN)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)

#changes frequency of the motors (how fast the electric signal is sent)
MAf = GPIO.PWM(8, frequency)
MAb = GPIO.PWM(7, frequency)
MBf = GPIO.PWM(10, frequency)
MBb = GPIO.PWM(9, frequency)

#changes the duty cycle 9speed of motors) to start at 0
MAf.start(0)
MAb.start(0)
MBf.start(0)
MBb.start(0)
#funtion to stop motors
def stop():
    MAf.ChangeDutyCycle(0)
    MAb.ChangeDutyCycle(0)
    MBf.ChangeDutyCycle(0)
    MBb.ChangeDutyCycle(0)

#function to move motors forward
def forward():
    MAf.ChangeDutyCycle(dutyCycleA)
    MAb.ChangeDutyCycle(0)
    MBf.ChangeDutyCycle(dutyCycleB)
    MBb.ChangeDutyCycle(0)

#function to move motors backward
def back():
    MAf.ChangeDutyCycle(0)
    MAb.ChangeDutyCycle(dutyCycleA)
    MBf.ChangeDutyCycle(0)
    MBb.ChangeDutyCycle(dutyCycleB)

#function to move motors left
def left():
    MAf.ChangeDutyCycle(0)
    MAb.ChangeDutyCycle(dutyCycleA)
    MBf.ChangeDutyCycle(dutyCycleB)
    MBb.ChangeDutyCycle(0)

#function to move motors right
def right():
    MAf.ChangeDutyCycle(dutyCycleA)
    MAb.ChangeDutyCycle(0)
    MBf.ChangeDutyCycle(0)
    MBb.ChangeDutyCycle(dutyCycleB)

#function to sense if it is near an object
def IsNearObject(localHowNear):
    Distance = measure()
    if Distance < localHowNear:
        return True
    else:
        return False

#function to measure distance
def measure():
    GPIO.output(pT, True)
    time.sleep(0.00001)
    GPIO.output(pT, False)
    startTime = time.time()
    stopTime = startTime
    while GPIO.input(pE) == 0:
        startTime = time.time()
        stopTime = startTime
    while GPIO.input(pE) == 1:
        stopTime = time.time()
        if stopTime - startTime >= 0.04:
            stopTime = startTime
            break
    totalTime = stopTime - startTime
    dist = totalTime * 34300
    dist = dist / 2
    return dist

#function to avoid obstacle
def AvoidObstacle():
    back()
    time.sleep(0.5)
    stop()
    right()
    time.sleep(0.75)
    stop()

#try portion of loop will infinatly move forward untill it senses an object
#if it does sense an object it will avoid it
try:
    GPIO.output(pT, False)
    time.sleep(0.1)
    while True:
        forward()
        time.sleep(0.1)
        if IsNearObject(HowNear):
            stop()
            AvoidObstacle()
#will shutdown program and turn off all motors
except KeyboardInterrupt:
    GPIO.cleanup()
        
