import RPi.GPIO as GPIO
from time import sleep
import threading



class temperatureSensor:
    def __init__(self, id, cs_pin, clk_pin, so_pin, lock):
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
        self.temperature = 0
        self.unit = "Celsius"
        self.lock = lock
        self.thread = threading.Thread(target=self.sense)
        self.thread.daemon = True
        self.thread.start()
        return

    def get_temperature(self) -> float:
        self.lock.acquire()
        GPIO.output(self.cs_pin,GPIO.HIGH)
        sleep(0.5)
        GPIO.output(self.cs_pin,GPIO.LOW)
        n = 16
        b = ""
        while n:
            GPIO.output(self.clk_pin,GPIO.HIGH)
            b += str(GPIO.input(self.so_pin))
            GPIO.output(self.clk_pin,GPIO.LOW)
            n -= 1
        self.temperature = int(b[1:-5], 2)+ int(b[-5])*0.5 + int(b[-4])*0.25
        self.lock.release()

    def sense(self):
        while True:
            self.get_temperature()
            sleep(0.1)

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
