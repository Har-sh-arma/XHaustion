import time
import os

num_minutes_in_accumulator = 60
time_format = "%m-%d %H:%M:%S"
accumulated_filename_fmt = "%Y-%m"
hour_power_dict = {}

class accumulator():
    def run(self):
        # loop through the log files in powerlogs directory
        # calculate the total power usage
        # write the total power usage to the shared memory
        global hour_power_dict
        current_time = time.localtime()
        for file in os.listdir("./powerLogs"):
            if (file == "log"):
                continue
            file_time = time.strptime(file.removeprefix("log."), "%Y-%m-%d_%H")
            if(file_time.tm_hour >= current_time.tm_hour):
                continue
            else:
                if(file_time.tm_hour not in hour_power_dict):
                    hour_power_dict[file_time.tm_hour] = []
                with open(f"./powerLogs/{file}", "r") as power_log:
                    for line in power_log.readlines():
                        power = list(map(float, line.split("\t")[1].split(",")))
                        if hour_power_dict[file_time.tm_hour] == []:
                            hour_power_dict[file_time.tm_hour] = [0]*len(power)
                        hour_power_dict[file_time.tm_hour] = list(map(lambda x, y: x+y , hour_power_dict[file_time.tm_hour], power))
                # os.remove("./powerLogs/{file}")
            with open("./accumulated/accumulated.csv", "a") as accumulated_file:
                accumulated_file.write(f"{time.strftime("%m-%d_%H", file_time )},{",".join(list(map(str,hour_power_dict[file_time.tm_hour])))}\n")


if __name__ == "__main__":
    acc = accumulator()
    acc.run()
