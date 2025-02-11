from blockchain import blockexplorer
from quantum_api.utils.utils import setup_logging
import logging

logger = setup_logging()

def log_to_blockchain(operation: str, details: dict) -> str:
    """
    Log an operation to the blockchain.
    """
    try:
        # Dummy blockchain logging
        # In production, integrate with a real blockchain or DLT
        tx_hash = blockexplorer.tx(operation, details)
        return tx_hash
    except Exception as e:
        logger.error(f"Error logging to blockchain: {e}")
        raise RuntimeError("Error logging to blockchain: " + str(e))

def get_blockchain_log(tx_hash: str) -> dict:
    """
    Retrieve a log from the blockchain by transaction hash.
    """
    try:
        # Dummy retrieval
        # In production, integrate with a real blockchain or DLT
        log = blockexplorer.get(tx_hash)
        return log
    except Exception as e:
        logger.error(f"Error retrieving log from blockchain: {e}")
        raise RuntimeError("Error retrieving log from blockchain: " + str(e))
