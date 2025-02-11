import logging
from typing import Any

def setup_logging(log_level: str = 'INFO') -> logging.Logger:
    """
    Set up logging with the specified log level.
    """
    try:
        logging.basicConfig(level=log_level)
        logger = logging.getLogger(__name__)
        return logger
    except Exception as e:
        logging.error("Failed to set up logging: " + str(e))
        raise RuntimeError("Failed to set up logging: " + str(e))

def validate_input(data: Any, schema: Any) -> bool:
    """
    Validate input data against a given schema.
    """
    try:
        schema.validate(data)
        return True
    except Exception as e:
        logging.error(f"Input validation failed: {e}")
        return False

def validate_input(data: Any, schema: Any) -> bool:
    """
    Validate input data against a given schema.
    """
    try:
        schema.validate(data)
        return True
    except Exception as e:
        logging.error(f"Input validation failed: {e}")
        return False
