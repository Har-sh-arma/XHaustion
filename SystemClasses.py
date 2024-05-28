from Sensor import temperatureSensor, pressureSensor
import logging
logger = logging.getLogger("XHaustion")

class System:
    def __init__(self, config):
        self.config = config
        self.mode = config["mode"]
        if(config["has_intake"]=="True"):
            self.intake = Fan(1, config["passive_modes"]["default"]["fans"]["intake"])
        self.exhaust = Fan(0, config["passive_modes"]["default"]["fans"]["exhaust"]) 
        self.dampers = [Damper(i, config["passive_modes"]["default"]["dampers"][i]) for i in range(config["num_dampers"])]
        self.tempSensors = [temperatureSensor(i) for i in range(config["num_dampers"])]
        
    def log_fan_power(self ,temperature_i, power , temp_sensor, added_fan_power):
        if(self.exhaust.fan_speed == added_fan_power):
            return
        logger.debug(f"Temperature: {temperature_i} \t Power: {power} \t Hood: {temp_sensor.id}")
    def update(self):
        active_flag = False
        if(self.config["has_intake"]=="True"):
            if (self.config["override"]["fans"]["intake"]== "False"):
                # Query how does intake scale with the temperature?
                self.intake.set_fan_speed(self.config["passive_modes"]["default"]["fans"]["intake"])

        if(self.config["override"]["fans"]["exhaust"] == "False"):
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
                self.exhaust.set_fan_speed(self.config["passive_modes"]["default"]["fans"]["exhaust"])

            else:
                if power>100:
                    power = 100
                self.exhaust.set_fan_speed(power)

        for i in self.tempSensors:
             temperature_i = i.get_temperature()
             if(self.config["override"]["dampers"][i.id] == "False"):
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
                    self.dampers[i.id].set_damper_angle(self.config["passive_modes"]["default"]["dampers"][i.id])
        if (((self.mode == "passive") and (active_flag)) or ((self.mode == "active")and (not active_flag))):
            if(active_flag):
                self.mode = "active"
            else:
                self.mode = "passive"
            logger.info("System Mode: " + self.mode)


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

