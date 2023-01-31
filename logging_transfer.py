import logging


class LoggingService:

    def __init__(self):
        logging.basicConfig(filename='file_transfer.log',level=logging.INFO, 
                    format='%(asctime)s %(levelname)s %(name)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                   )
                   
    def log_info(self,message):
        logging.info(message)
    
    def log_error(self,message):
        logging.exception(message)
        

