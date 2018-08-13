import inspect
import logging
#import os


def CustomeLogger(logLevel=logging.DEBUG):
    #BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    #LOG_FILE = os.path.join(BASEDIR,'automation.log')
    
    
    #Gets the name of the class / method from where this method is called
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    logger.setLevel(logging.DEBUG)
    
    fileHandler = logging.FileHandler("automation.log", mode='a')
    fileHandler.setLevel(logLevel)
    
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    
    return logger
    
    
    