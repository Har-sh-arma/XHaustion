import json
import time
from SystemClasses import System

config = json.load(open("./config.json"))

if __name__ == "__main__":
    sys = System(config)
    while True:
        inp = input("Enter command: ")
        print(list(inp.split()))
        time.sleep(1)