import logging
import sys
from functools import wraps

# ANSI color codes for terminal output
LOG_COLORS = {
    "DEBUG": "\033[94m",  # Blue
    "INFO": "\033[92m",  # Green
    "WARNING": "\033[93m",  # Yellow
    "ERROR": "\033[91m",  # Red
    "CRITICAL": "\033[95m",  # Magenta
    "RESET": "\033[0m",  # Reset color
}


# Custom formatter with colors
class ColoredFormatter(logging.Formatter):
    def format(self, record):
        log_color = LOG_COLORS.get(record.levelname, LOG_COLORS["RESET"])
        reset = LOG_COLORS["RESET"]
        record.levelname = f"{log_color}{record.levelname}{reset}"
        return super().format(record)


# Create the logger
logger = logging.getLogger("Logger")
logger.setLevel(logging.DEBUG)

# Add handlers only once
if not logger.handlers:
    formatter = ColoredFormatter(
        fmt="%(asctime)s | %(levelname)-20s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)


# Decorator to log function entry/exit
def log_function(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.debug(
            f"Entering function: {func.__name__} with args: {args}, kwargs: {kwargs}"
        )
        try:
            result = func(*args, **kwargs)
            logger.debug(f"Exiting function: {func.__name__} with result: {result}")
            return result
        except Exception:
            logger.exception(f"Exception in function: {func.__name__}")
            raise

    return wrapper
