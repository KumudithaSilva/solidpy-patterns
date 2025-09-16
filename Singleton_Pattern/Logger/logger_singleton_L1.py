import logging
import threading

class SingletonLogger:
    _instance = None
    _lock = threading.Lock()

    @classmethod
    def get_instance(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = cls()
                cls._instance.initialize_logger()
            return cls._instance

    def initialize_logger(self):
        # Set up the logger
        self.logger = logging.getLogger("Singleton_Logger_L1")
        self.logger.setLevel(logging.DEBUG)

        # Create file handler and set its level to DEBUG
        file_handler = logging.FileHandler("basic_file.log")
        file_handler.setLevel(logging.DEBUG)

        # Create a console handler and set its level to INFO
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # Create formater and add it to both handlers
        formater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formater)
        console_handler.setFormatter(formater)

        # Add the handlers to the logger
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)


# Add loggers
logger = SingletonLogger().get_instance().logger
logger.debug("DEBUTING STARTED")
logger.info("INFORMATION RECEIVED")
logger.warning("WARNING RECEIVED")
logger.error("ERROR OCCURRED")
logger.critical("CRITICAL ALARM")