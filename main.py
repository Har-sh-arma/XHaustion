import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import json
from SystemClasses import System
import logging
import os
from logging.handlers import TimedRotatingFileHandler
import threading
from shared_memory_dict import SharedMemoryDict
import sys as system
import traceback
import math

# Number of Hoods is limited to 4 due to hardware constraints(PWM pins)

sys = None
time_format = "%m-%d %H:%M:%S"
formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(message)s', datefmt=time_format)

logger = logging.getLogger('XHaustion')
handler = logging.handlers.RotatingFileHandler('logs/ExhaustSystem.log', maxBytes=5000, backupCount=5)
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)
config = json.load(open("./config/config.json"))


powerLogger = logging.Logger('PowerLogger')
powerLogger.setLevel(25)
powerLogFormatter = logging.Formatter(fmt='%(asctime)s\t%(message)s', datefmt=time_format)
powerLogHandler = TimedRotatingFileHandler("powerLogs/log", "h", 1, 5)
powerLogHandler.setFormatter(powerLogFormatter)
powerLogger.addHandler(powerLogHandler)

class PowerLoggingThread():
    def __init__(self, system:System, delay:int):
        self.system = system
        self.delay = delay
        self.thread = threading.Thread(target=self.run)
        self.thread.daemon = True
        self.thread.start()

    def run(self):
        while True:
            time.sleep(self.delay)
            exhaustPower = self.system.config["exhaust_fan_power_consumption_curve"][ math.floor(abs(int(self.system.shm["exhaust"])-1)/(100/self.system.config["fan_step"]))]
            if(self.system.config["has_intake"]):
                intakePower = self.system.config["intake_fan_power_consumption_curve"][ math.floor(abs(int(self.system.shm["intake"])-1)/(100/self.system.config["fan_step"]))]
            powerLogger.log(25, f"{exhaustPower},{intakePower}")


class Watcher:
    # Set the directory on watch
    def __init__(self, path):
        self.observer = Observer()
        self.watchDirectory = path
    
    def run(self):
        global sys
        event_handler = Handler()
        self.observer.schedule(event_handler, self.watchDirectory, recursive = False)
        self.observer.start()
        try:
            while True:
                pass
                sys.update()
                time.sleep(1)
                print(sys.shm["temperatures"], sys.shm["exhaustPressure"])
                #time.sleep(15)
                #system.exit()
        except Exception as e:
            print(f"Error Detected: {e}")
            traceback.print_exception(e)
            sys.exhaustPressureSensor.thread.join()
            for i in sys.tempSensors:
                i.thread.join()
            for i in sys.dampers:
                i.thread.join()
            sys.exhaust.thread.join()
            if(sys.config["has_intake"]):
                sys.intake.thread.join()
            self.observer.stop()
            print("Observer Stopped")
            sys.shm.shm.close()
            sys.shm.shm.unlink()
            self.observer.join()
            #system.exit()
 
 
class Handler(FileSystemEventHandler):
 
    @staticmethod
    def on_modified(event):
        try:
            print(sys.shm)
            config = json.load(open("./config/config.json"))#add try except
            sys.config = config
            logger.info("System Config Changed")
        except json.decoder.JSONDecodeError:
            pass

        
 
             
 
if __name__ == '__main__':
    system_state = SharedMemoryDict('system_state', 1024)
    sys = System(config, system_state)
    logger.info("System Initialized Successfully")
    watch = Watcher(os.path.join( os.getcwd(), "config"))
    powerLoggerThread = PowerLoggingThread(sys, 5)
    watch.run()
