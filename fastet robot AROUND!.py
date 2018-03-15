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

MAf = 8
MAb = 7
MBf = 10
MBb = 9

def stop():
    GPIO.output(MAf, 0)
    GPIO.output(MAb, 0)
    GPIO.output(MBf, 0)
    GPIO.output(MBb, 0)

def forward():
    GPIO.output(MAf, 1)
    GPIO.output(MAb, 0)
    GPIO.output(MBf, 1)
    GPIO.output(MBb, 0)

def back():
    GPIO.output(MAf, 0)
    GPIO.output(MAb, 2)
    GPIO.output(MBf, 0)
    GPIO.output(MBb, 2)

def left():
    GPIO.output(MAf, 0)
    GPIO.output(MAb, 2)
    GPIO.output(MBf, 2)
    GPIO.output(MBb, 0)

def right():
    GPIO.output(MAf, 2)
    GPIO.output(MAb, 0)
    GPIO.output(MBf, 0)
    GPIO.output(MBb, 2)

try:
    while True:
        char = screen.getch()
        if char == ord('q'):
            break
        elif char == curses.KEY_UP:
            forward()
            time.sleep(0.1)
        elif char == curses.KEY_DOWN:
            back()
            time.sleep(0.1)
        elif char == curses.KEY_LEFT:
            left()
            time.sleep(0.1)
        elif char == curses.KEY_RIGHT:
            right()
            time.sleep(0.1)
        elif char == 10:
            stop()
            
finally:
    curses.nocbreak()
    screen.keypad(0)
    curses.echo()
    curses.endwin()
    GPIO.cleanup()
