import RPi.GPIO as GPIO
import time
import curses

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)

def off():
    GPIO.output(7, 0)
    GPIO.output(8, 0)
    GPIO.output(9, 0)
    GPIO.output(10, 0)

def forward():
    GPIO.output(7, 0)
    GPIO.output(8, 1)
    GPIO.output(9, 0)
    GPIO.output(10, 1)
    time.sleep(1)

off()
forward()
GPIO.cleanup()
