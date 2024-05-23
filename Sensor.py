class temperatureSensor:
    def __init__(self, id):
        self.id = id
        self.temperature = self.get_temperature()
        self.unit = "Celsius"

    def get_temperature(self) -> float:
        #Actual GPIO Program to get Temperature
        default_temp = 80
        # print(f"Temperature Sensor {self.id}: {default_temp}")
        return default_temp
    

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