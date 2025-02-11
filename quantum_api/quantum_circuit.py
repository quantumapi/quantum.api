from qiskit import QuantumCircuit, Aer, execute

def create_dynamic_quantum_circuit(gates, qubits):
    # Create an empty quantum circuit
    circuit = QuantumCircuit(qubits)

    for gate in gates:
        if gate['type'] == 'H':
            circuit.h(gate['target'])
        elif gate['type'] == 'X':
            circuit.x(gate['target'])
        elif gate['type'] == 'CX':
            circuit.cx(gate['control'], gate['target'])
        elif gate['type'] == 'RZ':
            circuit.rz(gate['angle'], gate['target'])

    circuit.measure_all()

    # Using Aer's statevector simulator for the enhanced execution
    simulator = Aer.get_backend('qasm_simulator')
    result = execute(circuit, simulator, shots=1024).result()
    counts = result.get_counts(circuit)

    return counts
