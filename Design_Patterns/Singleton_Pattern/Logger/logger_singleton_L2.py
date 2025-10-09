import logging
import threading


class SingletonMeta(type):
    _instance = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instance:
                cls._instance[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instance[cls]


class Logger(metaclass=SingletonMeta):
    _logger = None

    def __init__(self):
        self._initialize_logger()

    def _initialize_logger(self):
        # Set up the logger
        print("Initializing logger")
        self._logger = logging.getLogger("Singleton_Logger_L1")
        self._logger.setLevel(logging.DEBUG)

        # Create file handler and set its level to DEBUG
        file_handler = logging.FileHandler("basic_file.log")
        file_handler.setLevel(logging.DEBUG)

        # Create a console handler and set its level to INFO
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # Create formater and add it to both handlers
        formater = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        file_handler.setFormatter(formater)
        console_handler.setFormatter(formater)

        # Add the handlers to the logger
        self._logger.addHandler(file_handler)
        self._logger.addHandler(console_handler)

    def getLogger(self):
        return self._logger


# Add loggers
logger = Logger().getLogger()
logger.debug("DEBUTING STARTED")
logger.info("INFORMATION RECEIVED")
logger.warning("WARNING RECEIVED")
logger.error("ERROR OCCURRED")
logger.critical("CRITICAL ALARM")
