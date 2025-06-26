import logging
import os
import json

# ---Core Tasks---

# Set up basic logging
LOG_FILENAME = 'app.log'
logging.basicConfig(
    filename=LOG_FILENAME,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.info("Program started")

# Handle division errors
def handle_division():
    try:
        user_input = input("Enter a number to divide 100 by: ")
        number = float(user_input)
        result = 100 / number
        print(f"Result: {result}")
        logging.info("Division successful")
    except ZeroDivisionError:
        logging.error("Attempted division by zero")
        print("Error: Cannot divide by zero.")
    except ValueError:
        logging.error("Invalid input: not a number")
        print("Error: Invalid input, please enter a number.")
    finally:
        logging.info("Division operation completed")

handle_division()

# Handle file operations
def read_config():
    try:
        with open("config.json", "r") as f:
            config = json.load(f)
            logging.info("Config file loaded successfully")
            print("Config:", config)
    except FileNotFoundError as e:
        logging.error("File not found: config.json")
        logging.debug("Detailed error: %s", e)

read_config()

# Create and use a custom exception
class InvalidValueError(Exception):
    """Custom exception for invalid values."""
    pass

def validate_positive_number(value):
    if value <= 0:
        raise InvalidValueError("Value must be positive")
    return True

def handle_validation():
    try:
        value = float(input("Enter a positive number: "))
        validate_positive_number(value)
        logging.info("Validation successful")
        print("Validation passed.")
    except InvalidValueError as e:
        logging.warning(f"Validation failed: {e}")
        print("Validation Error:", e)
    except ValueError:
        logging.error("Invalid input: not a number")
        print("Error: Please enter a valid number.")

handle_validation()

# Implement different logging levels
def demonstrate_logging_levels():
    logging.debug("This is a DEBUG message (useful for troubleshooting).")
    logging.info("This is an INFO message (general operation).")
    logging.warning("This is a WARNING message (something unexpected happened).")
    logging.error("This is an ERROR message (a problem occurred).")
    logging.critical("This is a CRITICAL message (a major failure happened).")

demonstrate_logging_levels()

# ---Extention Tasks---

import logging
import logging.handlers
import json
import os

# Implement log rotation to manage log file size
log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

log_file = 'app.log'
log_handler = logging.handlers.RotatingFileHandler(
    log_file, maxBytes=10000, backupCount=3  # rotates after 10KB, keeps 3 backups
)
log_handler.setFormatter(log_formatter)
log_handler.setLevel(logging.DEBUG)

# Set up root logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(log_handler)

# Add console handler
console_handler = logging.StreamHandler()
console_handler.setFormatter(log_formatter)
console_handler.setLevel(logging.INFO)
logger.addHandler(console_handler)

logger.info("Program started with extended features")

# Create a context manager
class FileReader:
    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, 'r')
        logger.debug(f"Opened file: {self.filename}")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
            logger.debug(f"Closed file: {self.filename}")
        if exc_type:
            logger.error("Exception in FileReader context manager", exc_info=True)
        return True  # prevents propagation

# Custom exception
class InvalidValueError(Exception):
    pass

def validate_positive_number(value):
    if value <= 0:
        raise InvalidValueError("Value must be positive")
    return True

# Decorator for logging function calls and exceptions
def log_function(func):
    def wrapper(*args, **kwargs):
        logger.debug(f"Calling function: {func.__name__}")
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.exception(f"Exception in {func.__name__}: {e}")
            raise
    return wrapper

@log_function
def handle_division():
    try:
        user_input = input("Enter a number to divide 100 by: ")
        number = float(user_input)
        result = 100 / number
        print(f"Result: {result}")
        logger.info("Division successful")
    except ZeroDivisionError as e:
        logger.error("Division by zero", exc_info=True)
        print("Cannot divide by zero.")
    except ValueError as e:
        logger.error("Invalid input for division", exc_info=True)
        print("Please enter a valid number.")
    finally:
        logger.info("Division operation completed")

@log_function
def read_config():
    try:
        with FileReader("config.json") as f:
            config = json.load(f)
            print("Config loaded:", config)
            logger.info("Config file loaded")
    except FileNotFoundError as e:
        logger.error("Config file not found", exc_info=True)
    except json.JSONDecodeError as e:
        logger.error("Invalid JSON in config file", exc_info=True)

@log_function
def handle_validation():
    try:
        value = float(input("Enter a positive number: "))
        validate_positive_number(value)
        logger.info("Validation successful")
        print("Validation passed.")
    except InvalidValueError as e:
        logger.warning(f"Validation failed: {e}")
        print("Validation Error:", e)
    except ValueError:
        logger.error("Invalid input for validation", exc_info=True)
        print("Error: Please enter a valid number.")

@log_function
def demonstrate_logging_levels():
    logger.debug("DEBUG message: useful for developers.")
    logger.info("INFO message: general event logged.")
    logger.warning("WARNING message: something unexpected but recoverable.")
    logger.error("ERROR message: functionality might be affected.")
    logger.critical("CRITICAL message: program may crash or is unstable.")

# Exception chaining with `raise from`
@log_function
def chained_exception_demo():
    try:
        raise ValueError("Inner exception")
    except ValueError as ve:
        raise RuntimeError("Outer exception with context") from ve

# ==== Execute ====
if __name__ == "__main__":
    handle_division()
    read_config()
    handle_validation()
    demonstrate_logging_levels()
    try:
        chained_exception_demo()
    except Exception:
        logger.info("Handled chained exception")