from Sensor import temperatureSensor, pressureSensor
from watchdog.observers import Observer
import logging
logger = logging.getLogger("XHaustion")
from shared_memory_dict import SharedMemoryDict
import json
from actuator import Fan, Damper
import threading
import smbus




class System:
    def __init__(self, config, shm):
        self.shm = shm
        self.config = config
        self.i2c_bus = smbus.SMBus(1)
        self.shm["mode"] = "passive"
        self.shm["passive_mode"] = "default"
        self.shm["override"] = {"fans":{"exhaust": 0, "intake": 0}, "dampers": [0]*config["num_dampers"]}
        if(self.config["has_intake"]):
            self.intake = Fan(1, self.config["fan_pins"][1] ,self.config["passive_modes"][self.shm["passive_mode"]]["fans"]["intake"], self.config["fan_step"])
        self.exhaust = Fan(0, self.config["fan_pins"][0] , self.config["passive_modes"][self.shm["passive_mode"]]["fans"]["exhaust"], self.config["fan_step"]) 
        self.dampers = [Damper(i, self.config["passive_modes"][self.shm["passive_mode"]]["dampers"][i], self.config["pwm_pins"][i]) for i in range(self.config["num_dampers"])]
        i2c_Lock = threading.Lock()
        
        self.tempSensors = [temperatureSensor(i, self.i2c_bus, self.config["ADC_i2c_address"], self.config["ADC_channels"]["temperature"][i], i2c_Lock, self.config["temperature_offset"], self.config["temperature_scaling"]) for i in range(self.config["num_dampers"])]
        
        
        self.exhaustPressureSensor = pressureSensor(0, self.i2c_bus, self.config["ADC_i2c_address"], self.config["ADC_channels"]["exhaust_pressure"], i2c_Lock, self.config["pressure_offset"], self.config["pressure_scaling"])
        
        self.init_sys_state()
    
    def init_sys_state(self):
        if(self.config["has_intake"]):
            self.shm["intake"] = self.intake.fan_speed
        
        self.shm["exhaust"] = self.exhaust.fan_speed
        self.shm["dampers"] = [i.damper_angle for i in self.dampers]
        self.shm["temperatures"] = [i.temperature for i in self.tempSensors]
        self.shm["exhaustPressure"] = self.exhaustPressureSensor.pressure

    def update(self):


        #Fan zone
        active_flag = False
        if(self.config["has_intake"]):
            if (not self.shm["override"]["fans"]["intake"]):
                power = 0
                for i in self.tempSensors:
                    temperature_i = i.temperature
                    l = len(self.config["temperature_range"])
                    while(l):
                        if(temperature_i > self.config["temperature_range"][l-1]):
                            power+= self.config["intake_fan_power_scaling_for_hoods"][i.id][l-1]
                            break
                        l-=1
                #check for exhaust pressure
                l = len(self.config["exhaust_pressure_range"])
                while(l):
                    if(self.shm["exhaustPressure"] > self.config["exhaust_pressure_range"][l-1]):
                        if(self.config["intake_fan_power_scaling_exhaust_pressure"][l-1] > power):
                            power= self.config["intake_fan_power_scaling_exhaust_pressure"][l-1]
                            break
                    l-=1

                if(power == 0):
                    self.intake.set_fan_speed(self.config["passive_modes"][self.shm["passive_mode"]]["fans"]["intake"])
                else:
                    if power>100:
                        power = 100
                    self.intake.set_fan_speed(power)
            else:
                self.intake.set_fan_speed(self.shm["intake"])

        if(not self.shm["override"]["fans"]["exhaust"]):
            # Adding the power according to each hood.
            # if multiple stations are active then the power will be scaled accordingly [can vary the way to scale]
            power = 0
            for i in self.tempSensors:
                temperature_i = i.temperature
                l = len(self.config["temperature_range"])
                while(l):
                    if(temperature_i > self.config["temperature_range"][l-1]):
                        power+= self.config["exhaust_fan_power_scaling_for_hoods"][i.id][l-1]
                        active_flag = True
                        break
                    l-=1
            #check for exhaust pressure
            l = len(self.config["exhaust_pressure_range"])
            while(l):
                if(self.shm["exhaustPressure"] > self.config["exhaust_pressure_range"][l-1]):
                    if(self.config["exhaust_fan_power_scaling_exhaust_pressure"][l-1] > power):
                        power= self.config["exhaust_fan_power_scaling_exhaust_pressure"][l-1]
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

        
        #Damper zone
        for i in self.tempSensors:
             temperature_i = i.temperature
             if( not self.shm["override"]["dampers"][i.id]):
                l = len(self.config["temperature_range"])
                default_damper = True
                while(l):
                    if(temperature_i > self.config["temperature_range"][l-1]):
                        self.dampers[i.id].set_damper_angle((90/self.config["damper_step"])*(l-1))
                        active_flag = True
                        default_damper = False
                        break
                    l-=1
                if(default_damper):
                    self.dampers[i.id].set_damper_angle(self.config["passive_modes"][self.shm["passive_mode"]]["dampers"][i.id])
             else:
                self.dampers[i.id].set_damper_angle(self.shm["dampers"][i.id])


        #Mode zone
        if (((self.shm["mode"] == "passive") and (active_flag)) or ((self.shm["mode"] == "active")and (not active_flag))):
            if(active_flag):
                self.shm["mode"] = "active"
            else:
                self.shm["mode"] = "passive"
                self.shm["override"] = {"fans":{"exhaust": 0, "intake": 0}, "dampers": [0]*self.config["num_dampers"]}
                # so that changes to the system made while cooking are transient and if the over ride is done while the system is in passive mode they stay
            logger.info("System Mode: " + self.shm["mode"])

        self.shm["exhaustPressure"] = self.exhaustPressureSensor.pressure
        self.shm["temperatures"] = [i.temperature for i in self.tempSensors]
        self.shm["dampers"] = [i.damper_angle for i in self.dampers]
        self.shm["intake"] = self.intake.fan_speed
        self.shm["exhaust"] = self.exhaust.fan_speed


