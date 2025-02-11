from qiskit import QuantumCircuit, Aer, execute
import numpy as np

def establish_quantum_entanglement(particles):
    """Establish quantum entanglement between multiple particles"""
    circuit = QuantumCircuit(len(particles))
    circuit.h(0)
    for i in range(1, len(particles)):
        circuit.cx(0, i)
    
    simulator = Aer.get_backend('statevector_simulator')
    result = execute(circuit, simulator).result()
    return result.get_statevector()
