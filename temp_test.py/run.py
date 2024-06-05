import RPi.GPIO as GPIO
from time import sleep


GPIO.setwarnings(False)			#disable warnings
GPIO.setmode(GPIO.BOARD)		#set pin numbering system
GPIO.setup(38,GPIO.OUT)
GPIO.setup(40,GPIO.OUT)
GPIO.setup(37,GPIO.IN)


GPIO.output(38,GPIO.LOW)

n = 16
while n:
    GPIO.output(40,GPIO.HIGH)
    sleep(0.5)
    GPIO.output(40,GPIO.LOW)
    sleep(0.5)
    print(f"Bit {n}: {GPIO.input(37)}")
    n -= 1

GPIO.output(38,GPIO.HIGH)