from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field
from typing import List, Dict, Any
import logging
import os
from prometheus_client import start_http_server, Counter, Histogram
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import jwt
from datetime import datetime, timedelta
from quantum_api.quantum_circuit.quantum_circuit import create_error_corrected_circuit
from quantum_api.quantum_simulation.quantum_simulation import simulate_quantum_circuit
from quantum_api.ai_integration.ai_integration import load_model, ai_optimize_quantum_circuit
from quantum_api.security.security import encrypt_data, decrypt_data
from quantum_api.blockchain_integration.blockchain_integration import log_to_blockchain, get_blockchain_log
from quantum_api.utils.utils import setup_logging

SECRET_KEY = os.getenv("SECRET_KEY", "my_secret_key")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

logger = setup_logging()
app = FastAPI(title="Quantum.API Production", version="2.0.0")

# CORS Setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Prometheus Metrics
QUANTUM_REQUESTS = Counter("quantum_requests", "Number of Quantum API requests")
LATENCY = Histogram("quantum_request_latency", "Quantum request latency")

@app.post("/simulate_quantum_circuit")
def simulate(request: Dict[str, Any], token: dict = Depends(verify_token)):
    QUANTUM_REQUESTS.inc()
    with LATENCY.time():
        try:
            circuit = create_error_corrected_circuit(request["qubits"], request["gates"])
            result = simulate_quantum_circuit(circuit)
            return {"simulation_result": result}
        except Exception as e:
            logger.error(f"Simulation Error: {e}")
            raise HTTPException(status_code=500, detail=str(e))

@app.post("/ai_optimize_circuit")
def optimize(request: Dict[str, Any], token: dict = Depends(verify_token)):
    try:
        optimized_circuit = ai_optimize_quantum_circuit(request["circuit"])
        return {"optimized_circuit": optimized_circuit}
    except Exception as e:
        logger.error(f"AI Optimization Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/log_to_blockchain")
def blockchain_log(request: Dict[str, Any], token: dict = Depends(verify_token)):
    try:
        tx_hash = log_to_blockchain(request["data"], request["metadata"])
        return {"transaction_hash": tx_hash}
    except Exception as e:
        logger.error(f"Blockchain Logging Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/get_blockchain_log/{tx_hash}")
def get_log(tx_hash: str, token: dict = Depends(verify_token)):
    try:
        log_entry = get_blockchain_log(tx_hash)
        return {"log": log_entry}
    except Exception as e:
        logger.error(f"Blockchain Retrieval Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/token")
def generate_token(form_data: OAuth2PasswordRequestForm = Depends()):
    if form_data.username != "admin" or form_data.password != "password":
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = create_access_token({"sub": form_data.username})
    return {"access_token": access_token, "token_type": "bearer"}

# Start Prometheus metrics server
start_http_server(8001)
