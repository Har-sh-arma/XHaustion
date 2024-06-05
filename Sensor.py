import RPi.GPIO as GPIO
from time import sleep

class temperatureSensor:
    def __init__(self, id, cs_pin, clk_pin, so_pin):
        self.id = id
        self.cs_pin = cs_pin
        self.clk_pin = clk_pin
        self.so_pin = so_pin
        # self.temperature = self.get_temperature()
        GPIO.setwarnings(False)			#disable warnings
        GPIO.setmode(GPIO.BOARD)		#set pin numbering system
        GPIO.setup(cs_pin,GPIO.OUT)
        GPIO.setup(clk_pin,GPIO.OUT)
        GPIO.setup(so_pin,GPIO.IN)
        self.get_temperature()
        self.unit = "Celsius"

    def get_temperature(self) -> float:
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
        self.temperature = int(b[1:-5], 2)+ int(b[-5])*0.5 + int(b[-4])*0.25
        return self.temperature
    

class pressureSensor:
    def __init__(self, id):
        self.id = id
        self.pressure = self.get_pressure()
        self.unit = "Bar"

    def get_pressure(self) -> float:
        #Actual GPIO Program to get Pressure
        default_pressure = 1
        # print(f"Pressure Sensor {self.id}: {default_pressure}")
        return default_pressure