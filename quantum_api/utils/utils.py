import logging
from typing import Any

def setup_logging(log_level: str = 'INFO'):
    logging.basicConfig(level=log_level)
    logger = logging.getLogger(__name__)
    return logger

def validate_input(data: Any, schema: Any) -> bool:
    try:
        schema.validate(data)
        return True
    except Exception as e:
        logging.error(f"Input validation failed: {e}")
        return False
