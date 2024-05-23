import json
from Unit import FanUnit, DamperUnit
import time


config = json.load(open("./config.json"))

fan = [FanUnit(i) for i in range(config["num_fans"])]
damper = [DamperUnit(i) for i in range(config["num_dampers"])]

if __name__ == "__main__":
    while True:
        print("Polling...")
        for i in range(config["num_fans"]):
            print(f"Fan {i} temperature: {fan[i].info()["temperature"]}")
                    
        time.sleep(1)