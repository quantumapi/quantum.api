# quantum_api/quantum_circuit/quantum_circuit.py
from typing import List, Dict, Any
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from quantum_api.utils.utils import setup_logging

logger = setup_logging()

def create_dynamic_quantum_circuit(gate_sequence: List[Dict[str, Any]], num_qubits: int) -> QuantumCircuit:
    """
    Create a quantum circuit based on a sequence of gate instructions.
    """
    try:
        qr = QuantumRegister(num_qubits, name="q")
        cr = ClassicalRegister(num_qubits, name="c")
        circuit = QuantumCircuit(qr, cr)
        for gate in gate_sequence:
            gate_type = gate.get('type')
            if gate_type == 'H':
                circuit.h(qr[gate['target']])
            elif gate_type == 'X':
                circuit.x(qr[gate['target']])
            elif gate_type == 'CX':
                circuit.cx(qr[gate['control']], qr[gate['target']])
            elif gate_type == 'Y':
                circuit.y(qr[gate['target']])
            elif gate_type == 'Z':
                circuit.z(qr[gate['target']])
            elif gate_type == 'S':
                circuit.s(qr[gate['target']])
            elif gate_type == 'T':
                circuit.t(qr[gate['target']])
            elif gate_type == 'SWAP':
                circuit.swap(qr[gate['control']], qr[gate['target']])
            elif gate_type == 'CCX':
                circuit.ccx(qr[gate['control1']], qr[gate['control2']], qr[gate['target']])
            else:
                raise ValueError(f"Unsupported gate type: {gate_type}")
        # Default measurement (could be made optional in production)
        circuit.measure(qr, cr)
        return circuit
    except Exception as e:
        logger.error(f"Error creating dynamic quantum circuit: {e}")
        raise RuntimeError("Error creating dynamic quantum circuit: " + str(e))

def apply_surface_code(circuit: QuantumCircuit) -> QuantumCircuit:
    """
    Apply a placeholder surface code error correction.
    In production, replace with a full error correction scheme.
    """
    try:
        # Add an ancillary register for error correction
        ancilla = QuantumRegister(1, name="ancilla")
        circuit.add_register(ancilla)
        # Placeholder: simple entanglement between the first qubit and the ancilla
        circuit.cx(circuit.qubits[0], ancilla[0])
        # Measure ancilla (for error syndrome extraction)
        creg = ClassicalRegister(1, name="c_ancilla")
        circuit.add_register(creg)
        circuit.measure(ancilla, creg)
        return circuit
    except Exception as e:
        logger.error(f"Error applying surface code: {e}")
        raise RuntimeError("Error applying surface code: " + str(e))

def create_error_corrected_circuit(gate_sequence: List[Dict[str, Any]], num_qubits: int) -> QuantumCircuit:
    """
    Build a dynamic circuit and then apply a surface code error correction scheme.
    """
    try:
        circuit = create_dynamic_quantum_circuit(gate_sequence, num_qubits)
        circuit = apply_surface_code(circuit)
        return circuit
    except Exception as e:
        logger.error(f"Error creating error-corrected circuit: {e}")
        raise RuntimeError("Error creating error-corrected circuit: " + str(e))
