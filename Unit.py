from Sensor import pressureSensor, temperatureSensor

class DamperUnit:
    def __init__(self, id:int):
        self.id = id
        self.angle=0
        self.pressure_sensor = pressureSensor(self.id)
        print(f"Damper {self.id} initialized")

    def set_angle(self, angle:int):
        #Actual GPIO Program to set Angle
        print(f"Damper {self.id} is set to {angle}")
        self.angle = angle

    def info(self) -> object:
        info = {
            "id": self.id,
            "angle": self.angle,
            "pressure": self.pressure_sensor.get_pressure()
        }
        return info

class FanUnit:
    def __init__(self, id:int):
        self.id = id
        self.fan_speed=0
        self.temperature_sensor = temperatureSensor(self.id)
        print(f"Fan {self.id} initialized")
    def set_speed(self, fan_speed:int):
        #Actual GPIO Program to set Angle
        print(f"Fan {self.id} is set to {fan_speed}")
        self.fan_speed = fan_speed

    def info(self) -> object:
        info = {
            "id": self.id,
            "angle": self.fan_speed,
            "temperature": self.temperature_sensor.get_temperature()
        }
        return info 




if __name__ == "__main__":
    print("Definition Package defining the classes for high modularity and Clearer Code.")