import RPi.GPIO as GPIO
from time import sleep


GPIO.setwarnings(False)			#disable warnings
GPIO.setmode(GPIO.BOARD)		#set pin numbering system
GPIO.setup(38,GPIO.OUT)
GPIO.setup(40,GPIO.OUT)


GPIO.output(38,GPIO.LOW)

n = 16
while n:
    GPIO.output(40,GPIO.HIGH)
    sleep(1)
    GPIO.output(40,GPIO.LOW)
    sleep(1)
    n -= 1

GPIO.output(38,GPIO.HIGH)