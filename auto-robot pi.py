import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(false)

pT = 17
pE = 18
GPIO.setup(pT, GPIO.OUT)
GPIO.setup(pE, GPIO.IN)
