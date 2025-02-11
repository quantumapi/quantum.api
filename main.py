# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Dict, Any
import logging
from prometheus_client import start_http_server, Counter, Histogram
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter

from quantum_api.quantum_circuit.quantum_circuit import create_error_corrected_circuit
from quantum_api.quantum_simulation.quantum_simulation import simulate_quantum_circuit
from quantum_api.ai_integration.ai_integration import load_model, ai_optimize_quantum_circuit
from quantum_api.security.security import encrypt_data, decrypt_data
from quantum_api.blockchain_integration.blockchain_integration import log_to_blockchain, get_blockchain_log
from quantum_api.utils.utils import setup_logging

logger = setup_logging()
app = FastAPI(title="Quantum.API Production", version="1.0.0")

# Prometheus metrics
REQUESTS = Counter('quantum_api_requests_total', 'Total number of requests')
LATENCY = Histogram('quantum_api_request_latency_seconds', 'Request latency')

# Set up OpenTelemetry tracing
trace.set_tracer_provider(TracerProvider())
span_exporter = OTLPSpanExporter(endpoint="http://localhost:4317")
span_processor = BatchSpanProcessor(span_exporter)
trace.get_tracer_provider().add_span_processor(span_processor)

class CircuitRequest(BaseModel):
    gate_sequence: List[Dict[str, Any]] = Field(..., example=[{"type": "H", "target": 0}])
    num_qubits: int = Field(..., gt=0)

class DataRequest(BaseModel):
    data: str

class BlockchainRequest(BaseModel):
    operation: str
    details: Dict[str, Any]

@app.post("/create_circuit")
async def create_circuit(request: CircuitRequest):
    REQUESTS.inc()
    with LATENCY.time():
        try:
            # In production, consider offloading CPU-bound work to a threadpool
            circuit = create_error_corrected_circuit(request.gate_sequence, request.num_qubits)
            return {"circuit": circuit.qasm()}
        except Exception as e:
            logger.error(f"Error in /create_circuit: {e}")
            raise HTTPException(status_code=500, detail=str(e))

@app.post("/simulate_circuit")
async def simulate_circuit(request: CircuitRequest):
    REQUESTS.inc()
    with LATENCY.time():
        try:
            circuit = create_error_corrected_circuit(request.gate_sequence, request.num_qubits)
            statevector = simulate_quantum_circuit(circuit)
            return {"statevector": statevector.tolist()}  # Convert numpy array to list
        except Exception as e:
            logger.error(f"Error in /simulate_circuit: {e}")
            raise HTTPException(status_code=500, detail=str(e))

@app.post("/optimize_circuit")
async def optimize_circuit(request: CircuitRequest):
    REQUESTS.inc()
    with LATENCY.time():
        try:
            model = load_model("default_model")
            circuit = create_error_corrected_circuit(request.gate_sequence, request.num_qubits)
            optimized_circuit = ai_optimize_quantum_circuit(circuit, model)
            return {"optimized_circuit": optimized_circuit.qasm()}
        except Exception as e:
            logger.error(f"Error in /optimize_circuit: {e}")
            raise HTTPException(status_code=500, detail=str(e))

@app.post("/encrypt")
async def encrypt_endpoint(request: DataRequest):
    REQUESTS.inc()
    with LATENCY.time():
        try:
            encrypted = encrypt_data(request.data)
            return {"encrypted_data": encrypted}
        except Exception as e:
            logger.error(f"Error in /encrypt: {e}")
            raise HTTPException(status_code=500, detail=str(e))

@app.post("/decrypt")
async def decrypt_endpoint(request: DataRequest):
    REQUESTS.inc()
    with LATENCY.time():
        try:
            decrypted = decrypt_data(request.data)
            return {"decrypted_data": decrypted}
        except Exception as e:
            logger.error(f"Error in /decrypt: {e}")
            raise HTTPException(status_code=500, detail=str(e))

@app.post("/log_to_blockchain")
async def blockchain_log(request: BlockchainRequest):
    REQUESTS.inc()
    with LATENCY.time():
        try:
            tx_hash = log_to_blockchain(request.operation, request.details)
            return {"tx_hash": tx_hash}
        except Exception as e:
            logger.error(f"Error in /log_to_blockchain: {e}")
            raise HTTPException(status_code=500, detail=str(e))

@app.get("/get_blockchain_log/{tx_hash}")
async def blockchain_get(tx_hash: str):
    REQUESTS.inc()
    with LATENCY.time():
        try:
            log_entry = get_blockchain_log(tx_hash)
            return {"log": log_entry}
        except Exception as e:
            logger.error(f"Error in /get_blockchain_log: {e}")
            raise HTTPException(status_code=500, detail=str(e))

# Start Prometheus metrics server
start_http_server(8001)
