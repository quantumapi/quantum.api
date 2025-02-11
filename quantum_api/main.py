# main.py
from fastapi import FastAPI, HTTPException
from quantum_api.quantum_computation import QuantumEngine
from quantum_api.utils.crypto import QuantumEncryption
from quantum_api.models import QuantumRequest, QuantumResponse
import logging

# Configure structured logging for production (expand with log handlers as needed)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Quantum API",
    version="2.0.0",
    description="A production–grade API for quantum–enhanced computing with robust encryption and scalable architecture."
)

# Instantiate our core modules
quantum_engine = QuantumEngine()
quantum_encryption = QuantumEncryption()

@app.post("/compute", response_model=QuantumResponse)
async def compute_quantum(request: QuantumRequest):
    """
    Endpoint to process quantum computations.
    Input data is validated via Pydantic models.
    The computed result is then encrypted before returning.
    """
    try:
        logger.info("Received compute request with data: %s", request.data)
        # Compute the quantum–inspired result
        raw_result = quantum_engine.compute(request.data)
        # Encrypt the result for secure transmission
        encrypted_result = quantum_encryption.encrypt(raw_result)
        return QuantumResponse(result=encrypted_result)
    except Exception as e:
        logger.exception("Error during computation")
        raise HTTPException(status_code=500, detail=f"Internal error: {str(e)}")

# Additional endpoints for decryption or other quantum services can be added here.
