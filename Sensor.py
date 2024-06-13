from time import sleep
import threading



class temperatureSensor:
    def __init__(self, id, smbus, smbus_address , channel,  lock, zero_offset, scaling):
        self.id = id
        self.smbus = smbus
        self.channel = channel
        self.smbus_address = int(smbus_address, 16)
        self.temperature = 0
        self.unit = "Celsius"
        self.lock = lock
        self.thread = threading.Thread(target=self.sense)
        self.thread.daemon = True
        self.thread.start()
        return

    def get_temperature(self) -> float:
        self.lock.acquire()
        self.smbus.bus.write_byte(self.smbus_address, self.channel)
        value = self.smbus.bus.read_byte(self.smbus_address)
        self.temperature = (value-self.zero_offset)*self.scaling
        self.lock.release()

    def sense(self):
        while True:
            self.get_temperature()
            sleep(0.1)

class pressureSensor:
    def __init__(self, id, smbus, smbus_address , channel,  lock, zero_offset, scaling):
        self.id = id
        self.pressure = 0
        self.unit = "Pascal"
        self.smbus = smbus
        self.lock = lock
        self.smbus_address = int(smbus_address, 16)
        self.zero_offset=zero_offset
        self.scaling=scaling
        self.channel = channel
        self.thread = threading.Thread(target=self.sense)
        self.thread.daemon = True
        self.thread.start()

    def get_pressure(self) -> float:
        self.lock.acquire()
        self.smbus.bus.write_byte(self.smbus_address, self.channel)
        value = self.smbus.bus.read_byte(self.smbus_address)
        self.pressure = (value-self.zero_offset)*self.scaling
        self.lock.release()
        return
    def sense(self):
        while True:
                self.get_pressure()
                sleep(0.1)

