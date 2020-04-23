#!/usr/bin/python3
import logging
from logging.handlers import TimedRotatingFileHandler
LOGFILE = '/var/log/mail_parser/logFile.log'
def setup_logger(module):
    logger = logging.getLogger(module)
    logger.setLevel(logging.DEBUG)
    handler = TimedRotatingFileHandler(LOGFILE,when='midnight',backupCount=5,encoding='utf-8')
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
