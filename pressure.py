
import smbus
import time
address = 0x48
A0 = 0x1a
zero_offset=60
scaling=12

bus = smbus.SMBus(1)

while True:
    bus.write_byte(address,A0)
    value = bus.read_byte(address)
    print((value-zero_offset)*scaling)
    time.sleep(0.1)
