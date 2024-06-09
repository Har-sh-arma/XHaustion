import logging
logger = logging.getLogger("XHaustion")
import threading
import RPi.GPIO as GPIO
from time import sleep


class Fan():

    def __init__(self, id , pin , default_speed ):
        self.id = id
        print(f"Fan {self.id} init")
        self.fan_speed = default_speed
        self.pin = pin
        self.set_fan_speed(default_speed)
        GPIO.setwarnings(False)			#disable warnings
        GPIO.setmode(GPIO.BOARD)		#set pin numbering system
        GPIO.setup(self.pin,GPIO.OUT)
        self.pi_pwm = GPIO.PWM(self.pin,1000)		#create PWM instance with frequency
        self.pi_pwm.start(0)
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
            self.pi_pwm.ChangeDutyCycle(int(self.fan_speed))
            sleep(1)
    
    def __str__(self) -> str:
        return str(self.id)

class Damper():

    def __init__(self, id, default_angle:int):
        self.id = id
        print(f"Damper {self.id} init")
        self.damper_angle = default_angle
        self.set_damper_angle(default_angle)
        pass
    def set_damper_angle(self, angle:int):
        #Actual GPIO Program to set damper angle
        if (self.damper_angle == angle):
            return
        logger.info(f"Damper {self.id} is set to {angle} degrees")
        self.damper_angle = angle
        pass
    def __str__(self) -> str:
        return str(self.id)
    

if __name__ == "__main__":
    print("Actuator Module")
