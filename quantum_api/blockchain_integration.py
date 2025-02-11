import hashlib
import json
import time
from typing import Dict, List
import logging
import os
import requests

# Configuration for blockchain integration
BLOCKCHAIN_API_URL = os.getenv('BLOCKCHAIN_API_URL', 'http://localhost:5000/api')
BLOCKCHAIN_API_KEY = os.getenv('BLOCKCHAIN_API_KEY', 'your_api_key_here')

_audit_log: List[Dict] = []

def log_operation(operation_name: str, data: dict) -> None:
    """
    Log an operation in a tamper-evident audit log using a real blockchain.
    """
    try:
        timestamp = time.time()
        entry = {
            "operation": operation_name,
            "data": data,
            "timestamp": timestamp,
            "prev_hash": _audit_log[-1]["hash"] if _audit_log else None
        }
        entry_str = json.dumps(entry, sort_keys=True)
        entry_hash = hashlib.sha256(entry_str.encode()).hexdigest()
        entry["hash"] = entry_hash
        _audit_log.append(entry)

        # Integrate with a real blockchain API
        response = requests.post(
            f"{BLOCKCHAIN_API_URL}/log_operation",
            json=entry,
            headers={"Authorization": f"Bearer {BLOCKCHAIN_API_KEY}"}
        )
        response.raise_for_status()
        logging.info("Operation logged in blockchain: " + response.text)
    except requests.RequestException as e:
        logging.error("Blockchain API request failed: " + str(e))
        raise RuntimeError("Blockchain API request failed: " + str(e))
    except Exception as e:
        logging.error("Failed to log operation: " + str(e))
        raise RuntimeError("Failed to log operation: " + str(e))
    """
    Log an operation in a tamper-evident audit log using a real blockchain.
    """
    try:
        timestamp = time.time()
        entry = {
            "operation": operation_name,
            "data": data,
            "timestamp": timestamp,
            "prev_hash": _audit_log[-1]["hash"] if _audit_log else None
        }
        entry_str = json.dumps(entry, sort_keys=True)
        entry_hash = hashlib.sha256(entry_str.encode()).hexdigest()
        entry["hash"] = entry_hash
        _audit_log.append(entry)

        # Placeholder for actual blockchain integration
        # Example: Use a blockchain API to log the operation
        # blockchain_api.log_operation(entry)
    except Exception as e:
        logging.error("Failed to log operation: " + str(e))
        raise RuntimeError("Failed to log operation: " + str(e))

def get_audit_log() -> List[Dict]:
    """
    Retrieve the current audit log.
    """
    try:
        return _audit_log
    except Exception as e:
        logging.error("Failed to retrieve audit log: " + str(e))
        raise RuntimeError("Failed to retrieve audit log: " + str(e))
    """
    Retrieve the current audit log.
    """
    try:
        return _audit_log
    except Exception as e:
        logging.error("Failed to retrieve audit log: " + str(e))
        raise RuntimeError("Failed to retrieve audit log: " + str(e))
