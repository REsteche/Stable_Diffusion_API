import logging
import graypy

class Logs:
    
    def __init__(self):
        logging.basicConfig(handlers=[logging.FileHandler(filename = "app/performance/logfile_ster.log", encoding='utf-8', mode = "w")],
                            format='%(asctime)s %(levelname)s %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')
        self.my_logger = logging.getLogger('test_logger')
        self.my_logger.setLevel(logging.DEBUG)
        handler = graypy.GELFUDPHandler('localhost', 12201)
        self.my_logger.addHandler(handler)
        
    def set_message(self, message, vars = []):
        
        if vars:
            self.my_logger.debug(message, *vars)
        else: 
            self.my_logger.debug(message)
        
        self.my_logger.debug(100*"-")
            
    
        