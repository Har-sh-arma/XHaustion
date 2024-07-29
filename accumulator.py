import threading.Thread as Thread
import time
import os

num_minutes_in_accumulator = 60
time_format = "%m-%d %H:%M:%S"


def accumulator(Thread):
    def run(self):
        # loop through the log files in powerlogs directory
        # calculate the total power usage
        # write the total power usage to the shared memory

        for file in os.listdir("./powerlogs"):
            print(file)

        current_time = time.time()


        