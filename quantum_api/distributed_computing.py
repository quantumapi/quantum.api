import blockchain
from qiskit import QuantumCircuit, transpile

def distribute_quantum_task(circuit, nodes):
    """Distribute quantum computation across blockchain nodes"""
    compiled_circuit = transpile(circuit, basis_gates=['u3', 'cx'])
    task = {
        'circuit': compiled_circuit,
        'shots': 1024,
        'nodes': nodes
    }
    blockchain.submit_task(task)
    return blockchain.monitor_task(task['id'])
