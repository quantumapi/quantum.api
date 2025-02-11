# main.py
import uvicorn
from fastapi import FastAPI, HTTPException, Depends, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List, Dict, Any
import logging

# Import configuration
from quantum_api.config.config import settings

# Import quantum modules (assumed to be production-ready or to be upgraded in parallel)
from quantum_api.quantum_circuit.quantum_circuit import (
    create_error_corrected_circuit,
    create_dynamic_quantum_circuit
)
from quantum_api.quantum_simulation.quantum_simulation import (
    simulate_quantum_circuit,
    hybrid_simulate
)
from quantum_api.ai_integration.ai_integration import load_model, ai_optimize_quantum_circuit
from quantum_api.security.security import encrypt_data, decrypt_data
from quantum_api.blockchain_integration.blockchain_integration import (
    log_to_blockchain,
    get_blockchain_log
)
from quantum_api.utils.utils import setup_logging

# Set up logging
logger = setup_logging(level=settings.log_level)

# Add global exception handler
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled exception: {exc}")
    return JSONResponse(
        status_code=500,
        content={"message": "Internal Server Error"},
    )

app = FastAPI(
    title="Quantum.API",
    description="The Quantum Revolution in Computing and Communication",
    version="2.0.0"
)

# Optional: Configure CORS (adjust allowed origins for production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Security: API Key Dependency
def verify_api_key(request: Request):
    api_key = request.headers.get("X-API-KEY")
    if api_key != settings.quantum_api_key:
        logger.warning("Unauthorized access attempt")
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid API Key")

# Request Models
class CircuitRequest(BaseModel):
    gate_sequence: List[Dict[str, Any]]
    num_qubits: int

class EncryptRequest(BaseModel):
    data: str

class DecryptRequest(BaseModel):
    encrypted_data: str

class BlockchainLogRequest(BaseModel):
    operation: str
    details: Dict[str, Any]

# Endpoints (all secured with API key dependency)
@app.post("/create_circuit/", dependencies=[Depends(verify_api_key)])
async def create_circuit(request: CircuitRequest):
    try:
        circuit = create_error_corrected_circuit(request.gate_sequence, request.num_qubits)
        return {"circuit": circuit}
    except Exception as e:
        logger.error(f"Error creating circuit: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/simulate_circuit/", dependencies=[Depends(verify_api_key)])
async def simulate_circuit(request: CircuitRequest):
    try:
        circuit = create_error_corrected_circuit(request.gate_sequence, request.num_qubits)
        statevector = simulate_quantum_circuit(circuit)
        return {"statevector": statevector}
    except Exception as e:
        logger.error(f"Error simulating circuit: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/optimize_circuit/", dependencies=[Depends(verify_api_key)])
async def optimize_circuit(request: CircuitRequest):
    try:
        model = load_model("default_model")
        circuit = create_error_corrected_circuit(request.gate_sequence, request.num_qubits)
        optimized_circuit = ai_optimize_quantum_circuit(circuit, model)
        return {"optimized_circuit": optimized_circuit}
    except Exception as e:
        logger.error(f"Error optimizing circuit: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/encrypt_data/", dependencies=[Depends(verify_api_key)])
async def encrypt_data_endpoint(request: EncryptRequest):
    try:
        encrypted = encrypt_data(request.data)
        return {"encrypted_data": encrypted}
    except Exception as e:
        logger.error(f"Error encrypting data: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/decrypt_data/", dependencies=[Depends(verify_api_key)])
async def decrypt_data_endpoint(request: DecryptRequest):
    try:
        decrypted = decrypt_data(request.encrypted_data)
        return {"decrypted_data": decrypted}
    except Exception as e:
        logger.error(f"Error decrypting data: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/log_to_blockchain/", dependencies=[Depends(verify_api_key)])
async def log_to_blockchain_endpoint(request: BlockchainLogRequest):
    try:
        tx_hash = log_to_blockchain(request.operation, request.details)
        return {"tx_hash": tx_hash}
    except Exception as e:
        logger.error(f"Error logging to blockchain: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/get_blockchain_log/", dependencies=[Depends(verify_api_key)])
async def get_blockchain_log_endpoint(tx_hash: str):
    try:
        log_entry = get_blockchain_log(tx_hash)
        return {"log": log_entry}
    except Exception as e:
        logger.error(f"Error retrieving blockchain log: {e}")
        raise HTTPException(status_code=500, detail=str(e))

# Additional endpoint for dynamic circuit creation (example)
@app.post("/create_dynamic_circuit/", dependencies=[Depends(verify_api_key)])
async def create_dynamic_circuit_endpoint(request: CircuitRequest):
    try:
        circuit = create_dynamic_quantum_circuit(request.gate_sequence, request.num_qubits)
        circuit_qasm = circuit.qasm()  # Assuming the circuit object supports QASM export
        return {"qasm": circuit_qasm}
    except Exception as e:
        logger.error(f"Error creating dynamic circuit: {e}")
        raise HTTPException(status_code=500, detail=str(e))

# Example endpoint for AI-driven simulation
@app.post("/simulate_with_ai/", dependencies=[Depends(verify_api_key)])
async def simulate_with_ai_endpoint(payload: Dict[str, Any]):
    try:
        quantum_state = payload.get('quantum_state')
        operator = payload.get('operator')
        # Load a pre-trained and secured AI model
        model = load_model("default_model")
        fidelity = hybrid_simulate(None, operator, model, quantum_state)
        return {"fidelity": fidelity}
    except Exception as e:
        logger.error(f"Error during AI simulation: {e}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    # Launch the production server using uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False, workers=settings.uvicorn_workers)
