import json
import time
from SystemClasses import System
import logging
import logging.handlers
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
time_format = "%m-%d %H:%M:%S"
formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(message)s', datefmt=time_format)

logger = logging.getLogger('XHaustion')
handler = logging.handlers.RotatingFileHandler('ExhaustSystem.log', maxBytes=5000, backupCount=5)
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)
config = json.load(open("./config.json"))

class LogHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print("Config Modified")
        logger.info("Config Modified")

if __name__ == "__main__":
    observer = Observer()
    observer.schedule(LogHandler(), path="./config.json", recursive=False)
    observer.start()
    sys = System(config)
    logger.info("System Initialized Successfully")
    while True:
        # inp = list(input("Enter command: ").split())
        # if(inp[0] == "T"):
            # sys.tempSensors[int(inp[1])].temperature = int(inp[2])
            # logger.info(f"Temperature for hood {inp[1]} set to {inp[2]} C")
            # print(f"Temperature for hood {inp[1]} set to {inp[2]} F")
        # sys.update()
        time.sleep(1)