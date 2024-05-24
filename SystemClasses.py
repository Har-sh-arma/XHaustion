from Sensor import temperatureSensor, pressureSensor


class System:
    def __init__(self, config):
        self.config = config
        if(config["has_intake"]=="True"):
            self.intake = Fan(1, config["passive_modes"]["default"]["fans"]["intake"])
        self.exhaust = Fan(0, config["passive_modes"]["default"]["fans"]["exhaust"]) 
        self.dampers = [Damper(i, config["passive_modes"]["default"]["dampers"][i]) for i in range(config["num_dampers"])]
        self.tempSensors = [temperatureSensor(i) for i in range(config["num_dampers"])]
        

    def update(self):
        if(self.config["has_intake"]==True):
            if (not self.config["override"]["intake"]):
                # Change Fan speed according to parameters
                pass
        if(not self.config["override"]["exhaust"]):
            #change the Exhaust fan acc to params
            pass
        for i in range(self.config["num_dampers"]):
            if(not self.config["override"]["dampers"][i]):
                #Change the dampers acc to params
                pass

class Fan():

    def __init__(self, id , default_speed:list):
        self.id = id
        print(f"Fan {id} is set to {default_speed}%")
        self.fan_speed = default_speed
        pass
    def set_fan_speed(self, fan_speed_percentage:int):
        #Actual GPIO Program to set fan Speed
        print(f"Fan {self.id} is set to {fan_speed_percentage}%")
        self.fan_speed = fan_speed_percentage


class Damper():

    def __init__(self, id, default_angle:int):
        self.id = id
        print(f"Damper {id} is set to {default_angle}%")
        self.damper_angle = default_angle
        pass
    def set_damper_angle(self, angle:int):
        pass

