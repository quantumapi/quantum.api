# quantum_api/tests/test_quantum_api.py
import json
from quantum_api.quantum_computation import run_quantum_circuit

def test_run_quantum_circuit():
    circuit = {
        "num_qubits": 2,
        "gates": [
            {"name": "h", "target": 0},
            {"name": "cx", "control": 0, "target": 1}
        ]
    }
    circuit_str = json.dumps(circuit)
    counts = run_quantum_circuit(circuit_str)
    # Verify that the result is a dictionary with expected measurement outcomes.
    assert isinstance(counts, dict)
    # Optionally add more assertions based on expected distributions.
