# quantum_api/quantum_api.py
from fastapi import FastAPI, HTTPException
from quantum_api.quantum_computation import run_quantum_circuit
from quantum_api.config import config
import logging

app = FastAPI(
    title="Supreme Quantum API",
    description="Production-grade API for quantum computing, integrating advanced simulation and quantum-safe security.",
    version="2.0.0"
)

# Setup logging
logging.basicConfig(level=logging.INFO)

@app.get("/simulate", summary="Simulate a Quantum Circuit")
def simulate_quantum_circuit(circuit: str):
    """
    Accepts a JSON-formatted string defining the quantum circuit.
    Example JSON:
    {
        "num_qubits": 2,
        "gates": [
            {"name": "h", "target": 0},
            {"name": "cx", "control": 0, "target": 1}
        ]
    }
    """
    try:
        result = run_quantum_circuit(circuit)
        return {"result": result}
    except Exception as e:
        logging.exception("Error during quantum circuit simulation.")
        raise HTTPException(status_code=500, detail=f"Quantum simulation error: {str(e)}")
