# quantum_api/quantum_computation.py
import json
from qiskit import QuantumCircuit, Aer, execute
import logging

def run_quantum_circuit(circuit_data: str) -> dict:
    """
    Create and execute a quantum circuit from a JSON string.

    :param circuit_data: JSON string containing circuit definition.
    :return: Dictionary with measurement counts.
    """
    try:
        circuit_params = json.loads(circuit_data)
    except json.JSONDecodeError as e:
        logging.error("Invalid JSON provided for circuit data.")
        raise ValueError("Invalid JSON input.") from e

    num_qubits = circuit_params.get("num_qubits", 2)
    qc = QuantumCircuit(num_qubits, num_qubits)

    # Example: Parse and add gates based on provided parameters.
    for gate in circuit_params.get("gates", []):
        if gate["name"].lower() == "h":
            qc.h(gate["target"])
        elif gate["name"].lower() == "cx":
            qc.cx(gate["control"], gate["target"])
        # Extend with additional gate parsing as needed.
        else:
            logging.warning(f"Unsupported gate '{gate['name']}' encountered.")

    qc.measure(range(num_qubits), range(num_qubits))

    backend = Aer.get_backend("qasm_simulator")
    job = execute(qc, backend, shots=1024)
    result = job.result()
    counts = result.get_counts(qc)
    logging.info("Quantum circuit executed successfully.")
    return counts
