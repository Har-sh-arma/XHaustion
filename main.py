import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import json
from SystemClasses import System
import logging
import logging.handlers
import os
from shared_memory_dict import SharedMemoryDict

sys = None
time_format = "%m-%d %H:%M:%S"
formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(message)s', datefmt=time_format)

logger = logging.getLogger('XHaustion')
handler = logging.handlers.RotatingFileHandler('logs/ExhaustSystem.log', maxBytes=5000, backupCount=5)
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)
config = json.load(open("./config/config.json"))



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
                sys.tempSensors[0].temperature = 25
                print("...Running..")
                print(system_state)
                sys.update()
                time.sleep(1)
        except:
            self.observer.stop()
            print("Observer Stopped")
        self.observer.join()
 
 
class Handler(FileSystemEventHandler):
 
    @staticmethod
    def on_modified(event):
        try:
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
    watch.run()
