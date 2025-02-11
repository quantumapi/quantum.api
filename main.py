from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any
from quantum_api.quantum_circuit.quantum_circuit import create_error_corrected_circuit
from quantum_api.quantum_simulation.quantum_simulation import simulate_quantum_circuit
from quantum_api.ai_integration.ai_integration import load_model, ai_optimize_quantum_circuit
from quantum_api.security.security import encrypt_data, decrypt_data
from quantum_api.blockchain_integration.blockchain_integration import log_to_blockchain, get_blockchain_log
from quantum_api.utils.utils import setup_logging

app = FastAPI()
logger = setup_logging()

class CircuitRequest(BaseModel):
    gate_sequence: List[Dict[str, Any]]
    num_qubits: int

@app.post("/create_circuit/")
async def create_circuit(request: CircuitRequest):
    try:
        circuit = create_error_corrected_circuit(request.gate_sequence, request.num_qubits)
        return {"circuit": circuit}
    except Exception as e:
        logger.error(f"Error creating circuit: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/simulate_circuit/")
async def simulate_circuit(request: CircuitRequest):
    try:
        circuit = create_error_corrected_circuit(request.gate_sequence, request.num_qubits)
        statevector = simulate_quantum_circuit(circuit)
        return {"statevector": statevector}
    except Exception as e:
        logger.error(f"Error simulating circuit: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/optimize_circuit/")
async def optimize_circuit(request: CircuitRequest):
    try:
        model = load_model("default_model")
        circuit = create_error_corrected_circuit(request.gate_sequence, request.num_qubits)
        optimized_circuit = ai_optimize_quantum_circuit(circuit, model)
        return {"optimized_circuit": optimized_circuit}
    except Exception as e:
        logger.error(f"Error optimizing circuit: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/encrypt_data/")
async def encrypt_data_endpoint(data: str):
    try:
        encrypted_data = encrypt_data(data)
        return {"encrypted_data": encrypted_data}
    except Exception as e:
        logger.error(f"Error encrypting data: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/decrypt_data/")
async def decrypt_data_endpoint(encrypted_data: str):
    try:
        decrypted_data = decrypt_data(encrypted_data)
        return {"decrypted_data": decrypted_data}
    except Exception as e:
        logger.error(f"Error decrypting data: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/log_to_blockchain/")
async def log_to_blockchain_endpoint(operation: str, details: Dict[str, Any]):
    try:
        tx_hash = log_to_blockchain(operation, details)
        return {"tx_hash": tx_hash}
    except Exception as e:
        logger.error(f"Error logging to blockchain: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/get_blockchain_log/")
async def get_blockchain_log_endpoint(tx_hash: str):
    try:
        log = get_blockchain_log(tx_hash)
        return {"log": log}
    except Exception as e:
        logger.error(f"Error retrieving log from blockchain: {e}")
        raise HTTPException(status_code=500, detail=str(e))
