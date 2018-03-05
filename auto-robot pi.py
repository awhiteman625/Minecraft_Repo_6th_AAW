import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pT = 17
pE = 18
GPIO.setup(pT, GPIO.OUT)
GPIO.setup(pE, GPIO.IN)

try:
    while True:
        GPIO.output(pT, False)
        time.sleep(0.5)
        GPIO.output(pT, True)
        time.sleep(0.00001)
        GPIO.output(pT, False)
        startTime = time.time()
        while GPIO.input(pE) == 0:
            startTime = time.time()
        while GPIO.input(pE) == 1:
            stopTime = time.time()
            if stopTime - startTime >= 0.04:
                print("you are to close")
                stopTime = startTime
                break

        totalTime = stopTime - startTime
        dist = totalTime * 34300
        dist = dist / 2
        print("Distance: " + str(dist) + " mm")
        time.sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()
        
