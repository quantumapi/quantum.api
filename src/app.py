# app.py
import os
import logging
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from quantum import simulate_quantum_algorithm
from encryption import encrypt_data, decrypt_data
from utils import setup_logging

# Initialize secure logging (production-grade logging format)
setup_logging()
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Quantum API Supreme",
    description="A production-ready API bridging quantum computing, secure cryptography, and scalable architectures.",
    version="2.0.0",
)

# Optional: Configure CORS if deploying in distributed environments.
app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.environ.get("ALLOWED_ORIGIN", "*")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/simulate", summary="Run a quantum simulation")
async def simulate(param: float = Query(..., gt=0.0, description="Quantum parameter (must be > 0)")):
    """
    Executes a quantum simulation and returns the encrypted result.
    """
    logger.info("Received simulation request with param: %s", param)
    try:
        result = simulate_quantum_algorithm(param)
        encrypted_result = encrypt_data(str(result))
        return {"encrypted_result": encrypted_result}
    except Exception as e:
        logger.exception("Simulation error encountered.")
        raise HTTPException(status_code=500, detail=f"Simulation error: {str(e)}")

@app.get("/decrypt", summary="Decrypt a simulation result")
async def decrypt(encrypted: str = Query(..., description="Encrypted result string")):
    """
    Decrypts the provided encrypted quantum result.
    """
    try:
        decrypted = decrypt_data(encrypted)
        return {"decrypted_result": decrypted}
    except Exception as e:
        logger.exception("Decryption error encountered.")
        raise HTTPException(status_code=500, detail=f"Decryption error: {str(e)}")

# Additional endpoints and production-level integrations can be added here.
