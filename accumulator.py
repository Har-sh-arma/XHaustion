import threading
import time
import os

num_minutes_in_accumulator = 60
time_format = "%m-%d %H:%M:%S"


class accumulator():
    def run(self):
        # loop through the log files in powerlogs directory
        # calculate the total power usage
        # write the total power usage to the shared memory

        current_time = time.time()
        hour_power_dict = {}
        for file in os.listdir("./powerlogs"):
            if (file == "log"):
                continue
            file_time = time.strptime(file.removeprefix("log."), "%Y-%m-%d_%H-%M")
            if(file_time.tm_hour >= current_time.tm_hour):
                continue

if __name__ == "__main__":
    acc = accumulator()
    acc.run()
