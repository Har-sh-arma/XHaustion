import RPi.GPIO as GPIO
from time import sleep


GPIO.setwarnings(False)			#disable warnings
GPIO.setmode(GPIO.BOARD)		#set pin numbering system
GPIO.setup(38,GPIO.OUT)
GPIO.setup(40,GPIO.OUT)
GPIO.setup(37,GPIO.IN)



while True:
    GPIO.output(38,GPIO.HIGH)
    sleep(0.5)
    GPIO.output(38,GPIO.LOW)
    b=""
    n = 16
    while n:
        GPIO.output(40,GPIO.HIGH)
        sleep(0.01)
        b += str(GPIO.input(37))
        GPIO.output(40,GPIO.LOW)
        sleep(0.01)
        n -= 1

    print(int(b[1:-5], 2)+ int(b[-5])*0.5 + int(b[-4])*0.25)
