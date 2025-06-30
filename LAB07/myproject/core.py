"""
Core utility functions.
"""
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def say_hello(name):
    logger.info(f"Saying hello to {name}")
    return f"Hello, {name}!"

def get_timestamp():
    """
    Returns the current timestamp in ISO format.
    """
    from datetime import datetime
    return datetime.now().isoformat()
