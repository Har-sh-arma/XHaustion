import logging
logger = logging.getLogger("XHaustion")
import threading
import RPi.GPIO as GPIO
from time import sleep
import math


class Fan():

    def __init__(self, id , pins , default_speed , fan_step):
        self.id = id
        print(f"Fan {self.id} init")
        self.fan_step = fan_step
        self.fan_speed = default_speed
        self.pins = pins
        self.set_fan_speed(default_speed)
        GPIO.setwarnings(False)			#disable warnings
        GPIO.setmode(GPIO.BOARD)		#set pin numbering system
        GPIO.setup(self.pins[0],GPIO.OUT)
        GPIO.setup(self.pins[1],GPIO.OUT)
        # self.pi_pwm = GPIO.PWM(self.pin,1000)		#create PWM instance with frequency
        # self.pi_pwm.start(0)
        self.thread = threading.Thread(target=self.start)
        self.thread.daemon = True
        self.thread.start()
    
    def set_fan_speed(self, fan_speed_percentage:int):
        #Actual GPIO Program to set fan Speed
        if (self.fan_speed == fan_speed_percentage):
            return
        logger.info(f"Fan {self.id}: set to {fan_speed_percentage}%")
        self.fan_speed = fan_speed_percentage
    
    def start(self):
        while True:
            # PUll gpio pin high
            if int(str(bin(math.floor(abs(int(self.fan_speed)-1)/(100/self.fan_step)))).split("b")[-1][-1]):
                GPIO.output(self.pins[0],GPIO.HIGH)
            else:
                GPIO.output(self.pins[0],GPIO.LOW)
            try:
                if int(str(bin(math.floor(abs(int(self.fan_speed)-1)/(100/self.fan_step)))).split("b")[-1][-2]):
                    GPIO.output(self.pins[1],GPIO.HIGH)
                else:
                    GPIO.output(self.pins[1],GPIO.LOW)
            except IndexError:
                GPIO.output(self.pins[1],GPIO.LOW)


    def __str__(self) -> str:
        return str(self.id)

class Damper():

    def __init__(self, id, default_angle:int, pin):
        self.id = id
        print(f"Damper {self.id} init on {pin}")
        self.damper_angle = default_angle
        self.pin = pin
        self.set_damper_angle(default_angle)
        GPIO.setwarnings(False)			#disable warnings
        GPIO.setmode(GPIO.BOARD)		#set pin numbering system
        GPIO.setup(self.pin,GPIO.OUT)
        self.pi_pwm = GPIO.PWM(self.pin,1000)		#create PWM instance with frequency
        self.pi_pwm.start(0)
        self.thread = threading.Thread(target=self.start)
        self.thread.daemon = True
        self.thread.start()
    def set_damper_angle(self, angle:int):
        if (self.damper_angle == angle):
            return
        logger.info(f"Damper {self.id} is set to {angle} degrees")
        self.damper_angle = angle
    def start(self):
        while True:
            print(((int(self.damper_angle)/90)*100))
            self.pi_pwm.ChangeDutyCycle(((int(self.damper_angle)/90)*100))
            sleep(1)    
    def __str__(self) -> str:
        return str(self.id)
    

if __name__ == "__main__":
    print("Actuator Module")
