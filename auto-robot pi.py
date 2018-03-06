import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pT = 17
pE = 18
HowNear = 15.0
frequency = 20
dutyCycleA = 50
dutyCycleB = 40

GPIO.setup(pT, GPIO.OUT)
GPIO.setup(pE, GPIO.IN)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)

MAf = GPIO.PWM(8, frequency)
MAb = GPIO.PWM(7, frequency)
MBf = GPIO.PWM(10, frequency)
MBb = GPIO.PWM(9, frequency)

MAf.start(0)
MAb.start(0)
MBf.start(0)
MBb.start(0)

def stop():
    MAf.ChangeDutyCycle(0)
    MAb.ChangeDutyCycle(0)
    MBf.ChangeDutyCycle(0)
    MBb.ChangeDutyCycle(0)

def forward():
    MAf.ChangeDutyCycle(dutyCycleA)
    MAb.ChangeDutyCycle(0)
    MBf.ChangeDutyCycle(dutyCycleB)
    MBb.ChangeDutyCycle(0)

def back():
    MAf.ChangeDutyCycle(0)
    MAb.ChangeDutyCycle(dutyCycleA)
    MBf.ChangeDutyCycle(0)
    MBb.ChangeDutyCycle(dutyCycleB)

def left():
    MAf.ChangeDutyCycle(0)
    MAb.ChangeDutyCycle(dutyCycleA)
    MBf.ChangeDutyCycle(dutyCycleB)
    MBb.ChangeDutyCycle(0)

def right():
    MAf.ChangeDutyCycle(dutyCycleA)
    MAb.ChangeDutyCycle(0)
    MBf.ChangeDutyCycle(0)
    MBb.ChangeDutyCycle(dutyCycleB)

def IsNearObject(localHowNear):
    Distance = measure()
    if Distance < localHowNear:
        return True
    else:
        return False

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

def AvoidObstacle():
    back()
    time.sleep(0.5)
    stop()
    right()
    time.sleep(0.75)
    stop()


try:
    GPIO.output(pT, False)
    time.sleep(0.1)
    while True:
        forward()
        time.sleep(0.1)
        if IsNearObject(HowNear):
            stop()
            AvoidObstacle()
except KeyboardInterrupt:
    GPIO.cleanup()
        
