from Sensor import temperatureSensor, pressureSensor
from watchdog.observers import Observer
import logging
logger = logging.getLogger("XHaustion")
from shared_memory_dict import SharedMemoryDict
import asyncio
import json



'''

    Big change!!!  any issue pe first check this

    "mode": "passive",
    "passive_mode": "default",

    "override": {
        "fans": {
            "exhaust": 0,
            "intake": 0
        },
        "dampers": [
            0,
            0,
            0,
            0
        ]
    },

    moved to shm
'''

class System:
    def __init__(self, config, shm):
        self.shm = shm
        self.config = config
        self.shm["mode"] = "passive"
        self.shm["passive_mode"] = "default"
        self.shm["override"] = {"fans":{"exhaust": 0, "intake": 0}, "dampers": [0, 0, 0, 0]}
        if(self.config["has_intake"]):
            self.intake = Fan(1, self.config["passive_modes"][self.shm["passive_mode"]]["fans"]["intake"])
        self.exhaust = Fan(0, self.config["passive_modes"][self.shm["passive_mode"]]["fans"]["exhaust"]) 
        self.dampers = [Damper(i, self.config["passive_modes"][self.shm["passive_mode"]]["dampers"][i]) for i in range(self.config["num_dampers"])]
        self.tempSensors = [temperatureSensor(i) for i in range(self.config["num_dampers"])]
        self.init_sys_state()
    def init_sys_state(self):
        if(self.config["has_intake"]):
            self.shm["intake"] = self.intake.fan_speed
        self.shm["exhaust"] = self.exhaust.fan_speed
        self.shm["dampers"] = [i.damper_angle for i in self.dampers]
        self.shm["temperatures"] = [i.temperature for i in self.tempSensors]

    def update(self):
        active_flag = False
        if(self.config["has_intake"]):
            if (not self.shm["override"]["fans"]["intake"]):
                # Query how does intake scale with the temperature        ????? 
                self.intake.set_fan_speed(self.config["passive_modes"][self.shm["passive_mode"]]["fans"]["intake"])
            else:
                self.intake.set_fan_speed(self.shm["intake"])

        if(not self.shm["override"]["fans"]["exhaust"]):
            # Adding the power according to each hood.
            # if multiple stations are active then the power will be scaled accordingly [can vary the way to scale]
            power = 0
            for i in self.tempSensors:
                temperature_i = i.get_temperature()
                l = len(self.config["temperature_range"])
                while(l):
                    if(temperature_i > self.config["temperature_range"][l-1]):
                        power+= self.config["fan_power_scaling_for_hoods"][i.id][l-1]
                        active_flag = True
                        break
                    l-=1
            if(power == 0):
                self.exhaust.set_fan_speed(self.config["passive_modes"][self.shm["passive_mode"]]["fans"]["exhaust"])
            else:
                if power>100:
                    power = 100
                self.exhaust.set_fan_speed(power)
        else:
            self.exhaust.set_fan_speed(self.shm["exhaust"])
        for i in self.tempSensors:
             temperature_i = i.get_temperature()
             if( not self.shm["override"]["dampers"][i.id]):
                l = len(self.config["temperature_range"])
                default_damper = True
                while(l):
                    if(temperature_i > self.config["temperature_range"][l-1]):
                        self.dampers[i.id].set_damper_angle(self.config["damper_angles"][l-1])
                        active_flag = True
                        default_damper = False
                        break
                    l-=1
                if(default_damper):
                    
                    self.dampers[i.id].set_damper_angle(self.config["passive_modes"][self.shm["passive_mode"]]["dampers"][i.id])

        if (((self.shm["mode"] == "passive") and (active_flag)) or ((self.shm["mode"] == "active")and (not active_flag))):
            if(active_flag):
                self.shm["mode"] = "active"
            else:
                self.shm["mode"] = "passive"
                self.shm["override"] = {"fans": {"exhaust": 0, "intake": 0}, "dampers": [0, 0, 0, 0]} 
                # so that changes to the system made while cooking are transient and if the over ride is done while the system is in passive mode they stay
            logger.info("System Mode: " + self.shm["mode"])
        
        self.shm["temperatures"] = [i.temperature for i in self.tempSensors]
        self.shm["dampers"] = [i.damper_angle for i in self.dampers]
        self.shm["intake"] = self.intake.fan_speed
        self.shm["exhaust"] = self.exhaust.fan_speed


class Fan():

    def __init__(self, id , default_speed):
        self.id = id
        self.fan_speed = default_speed
        self.set_fan_speed(default_speed)
        pass
    def set_fan_speed(self, fan_speed_percentage:int):
        #Actual GPIO Program to set fan Speed
        if (self.fan_speed == fan_speed_percentage):
            return
        logger.info(f"Fan {self.id}: set to {fan_speed_percentage}%")
        self.fan_speed = fan_speed_percentage
    def __str__(self) -> str:
        return str(self.id)

class Damper():

    def __init__(self, id, default_angle:int):
        self.id = id
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

