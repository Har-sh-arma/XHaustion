import logging
import logging.handlers
import time
time_format = "%m-%d %H:%M:%S"
formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(message)s', datefmt=time_format)

logger = logging.getLogger('XHaustion')
handler = logging.handlers.RotatingFileHandler('XHaustion.log', maxBytes=1000, backupCount=5)
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)


while True:
    logger.debug('Logged Something')
    time.sleep(1)