#import all libraries needed
import RPi.GPIO as GPIO
import time
import curses

#set curses library up for our use
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

#set GPIO library and sets pins for our use
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)

#sets two variables name frequency and dutycycle, to better control robot speed
frequency = 20
dutyCycle = 50

#sets 4 variables to control each motor going forward and back with
#a specific frequency
MAf = GPIO.PWM(8, frequency)
MAb = GPIO.PWM(7, frequency)
MBf = GPIO.PWM(10, frequency)
MBb = GPIO.PWM(9, frequency)

#starts software with duty cylce of 0
MAf.start(0)
MAb.start(0)
MBf.start(0)
MBb.start(0)

#function to stop motors
def stop():
    MAf.ChangeDutyCycle(0)
    MAb.ChangeDutyCycle(0)
    MBf.ChangeDutyCycle(0)
    MBb.ChangeDutyCycle(0)

#function to push both motors forward
def forward():
    MAf.ChangeDutyCycle(dutyCycle)
    MAb.ChangeDutyCycle(0)
    MBf.ChangeDutyCycle(dutyCycle)
    MBb.ChangeDutyCycle(0)

#function to push both motors backwards
def back():
    MAf.ChangeDutyCycle(0)
    MAb.ChangeDutyCycle(dutyCycle)
    MBf.ChangeDutyCycle(0)
    MBb.ChangeDutyCycle(dutyCycle)
    
#function to push one motor forward and one backward
#causing it to turn left
def left():
    MAf.ChangeDutyCycle(0)
    MAb.ChangeDutyCycle(dutyCycle)
    MBf.ChangeDutyCycle(dutyCycle)
    MBb.ChangeDutyCycle(0)

#function to push one motor forward and on backward
    #causing it to turn right
def right():
    MAf.ChangeDutyCycle(dutyCycle)
    MAb.ChangeDutyCycle(0)
    MBf.ChangeDutyCycle(0)
    MBb.ChangeDutyCycle(dutyCycle)

#a try-finally loop that will try the top portion, untl is is not true
    #and then continue on the the bottom portion
try:
    #an infinite while loop used to call specific functions when a
    #specific key is pressed. will break if you press "q"
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
    #this portion of the try-finally loop will cleanup the
    #GPIO pins and set curses back to normal
    curses.nocbreak()
    screen.keypad(0)
    curses.echo()
    curses.endwin()
    GPIO.cleanup()
