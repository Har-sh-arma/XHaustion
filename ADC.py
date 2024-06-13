import RPi.GPIO as GPIO
from time import sleep
import threading
import smbus



address = 0x48
bus = smbus.SMBus(1)
bus.write_byte(address, 0)
value = bus.read_byte(address)
print(f"{value}")

bus.write_byte(address, 1)
value = bus.read_byte(address)
print(f"{value}")



