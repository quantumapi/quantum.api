import hashlib
import json
import time
from typing import Dict, List
import logging

_audit_log: List[Dict] = []

def log_operation(operation_name: str, data: dict) -> None:
    """
    Log an operation in a tamper-evident audit log.
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
