import hashlib
import json
import time

# In a production environment, this would interface with a decentralized ledger.
# Here, we simulate a simple append-only audit log with hash chaining.

_audit_log = []

def log_operation(operation_name: str, data: dict) -> None:
    """
    Log an operation in a tamper-evident audit log.
    """
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

def get_audit_log() -> list:
    """
    Retrieve the audit log.
    """
    return _audit_log
