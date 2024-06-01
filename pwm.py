
import RPi.GPIO as GPIO
from time import sleep

ledpin = 32				# PWM pin connected to LED
GPIO.setwarnings(False)			#disable warnings
GPIO.setmode(GPIO.BOARD)		#set pin numbering system
GPIO.setup(ledpin,GPIO.OUT)
pi_pwm = GPIO.PWM(ledpin,1000)		#create PWM instance with frequency
pi_pwm.start(0)				#start PWM of required Duty Cycle 

while True:
    pi_pwm.ChangeDutyCycle(50) #provide duty cycle in the range 0-100
