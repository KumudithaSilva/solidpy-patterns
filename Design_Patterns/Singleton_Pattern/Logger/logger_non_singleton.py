import logging

# Set up the logger
logger = logging.getLogger("non_singleton_logger")
logger.setLevel(logging.DEBUG)

# Create file handler and set its level to DEBUG
file_handler = logging.FileHandler("basic_file.log")
file_handler.setLevel(logging.DEBUG)

# Create a console handler and set its level to INFO
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Create formater and add it to both handlers
formater = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formater)
console_handler.setFormatter(formater)

# Add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Add loggers
logger.debug("DEBUTING STARTED")
logger.info("INFORMATION RECEIVED")
logger.warning("WARNING RECEIVED")
logger.error("ERROR OCCURRED")
logger.critical("CRITICAL ALARM")
