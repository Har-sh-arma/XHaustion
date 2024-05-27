from Sensor import temperatureSensor, pressureSensor
import logging
logger = logging.getLogger("XHaustion")

class System:
    def __init__(self, config):
        self.config = config
        if(config["has_intake"]=="True"):
            self.intake = Fan(1, config["passive_modes"]["default"]["fans"]["intake"])
        self.exhaust = Fan(0, config["passive_modes"]["default"]["fans"]["exhaust"]) 
        self.dampers = [Damper(i, config["passive_modes"]["default"]["dampers"][i]) for i in range(config["num_dampers"])]
        self.tempSensors = [temperatureSensor(i) for i in range(config["num_dampers"])]
        

    def update(self):
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
                if(temperature_i >180):
                    power+= self.config["fan_power_scaling_for_hoods"][i.id][-1]
                    logger.debug(f"Temperature: {temperature_i} \t Power: {power} \t Hood: {i.id}")
                elif(temperature_i > 150):
                    power+= self.config["fan_power_scaling_for_hoods"][i.id][-2]
                    logger.debug(f"Temperature: {temperature_i} \t Power: {power} \t Hood: {i.id}")
                elif(temperature_i > 120):
                    power+= self.config["fan_power_scaling_for_hoods"][i.id][-3]
                    logger.debug(f"Temperature: {temperature_i} \t Power: {power} \t Hood: {i.id}")
                elif(temperature_i > 90):
                    power+= self.config["fan_power_scaling_for_hoods"][i.id][-4]
                    logger.debug(f"Temperature: {temperature_i} \t Power: {power} \t Hood: {i.id}")
            if(power == 0):
                self.exhaust.set_fan_speed(self.config["passive_modes"]["default"]["fans"]["exhaust"])
            else:
                if power>100:
                    power = 100
                self.exhaust.set_fan_speed(power)

        for i in self.tempSensors:
             temperature_i = i.get_temperature()
             if(self.config["override"]["dampers"][i.id] == "False"):
                if(temperature_i >180):
                    self.dampers[i.id].set_damper_angle(self.config["damper_angles"][-1])
                elif(temperature_i > 150):
                    self.dampers[i.id].set_damper_angle(self.config["damper_angles"][-2])
                elif(temperature_i > 120):
                    self.dampers[i.id].set_damper_angle(self.config["damper_angles"][-3])
                elif(temperature_i > 90):
                    self.dampers[i.id].set_damper_angle(self.config["damper_angles"][-4])
                else:
                    if(self.dampers[i.id].damper_angle == self.config["passive_modes"]["default"]["dampers"][i.id]):
                        continue
                    self.dampers[i.id].set_damper_angle(self.config["passive_modes"]["default"]["dampers"][i.id])


class Fan():

    def __init__(self, id , default_speed):
        self.id = id
        self.fan_speed = default_speed
        self.set_fan_speed(default_speed)
        pass
    def set_fan_speed(self, fan_speed_percentage:int):
        #Actual GPIO Program to set fan Speed
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
        logger.info(f"Damper {self.id} is set to {angle} degrees")
        self.damper_angle = angle
        pass

