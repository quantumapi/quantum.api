# utils.py
import logging

def setup_logging():
    """
    Configures structured logging for the application.
    """
    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
    )
