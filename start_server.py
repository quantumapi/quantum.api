from flask import Flask, request, jsonify
from quantum_api import quantum_circuit, quantum_simulation, ai_integration
import tensorflow as tf

app = Flask(__name__)

@app.route('/create_dynamic_circuit', methods=['POST'])
def create_dynamic_circuit_endpoint():
    try:
        data = request.get_json()
        gate_sequence = data['gates']  # Expecting a list of gate dictionaries
        num_qubits = data['qubits']      # Number of qubits in the circuit
        circuit = quantum_circuit.create_dynamic_quantum_circuit(gate_sequence, num_qubits)
        # Serialize the circuit (e.g., in QASM format) for client-side visualization
        circuit_qasm = circuit.qasm()
        return jsonify({"status": "success", "qasm": circuit_qasm})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

@app.route('/simulate_with_ai', methods=['POST'])
def simulate_with_ai_endpoint():
    try:
        data = request.get_json()
        quantum_state = data['quantum_state']  # Should be a list of complex numbers
        operator = data['operator']            # e.g., "X" or "H"
        ai_model_config = data.get('ai_model_config', {})  # Optional configuration

        # Load or build a dummy AI model.
        # In a production system, you would load a pre-trained, secured model.
        input_dim = len(quantum_state)
        ai_model = tf.keras.Sequential([
            tf.keras.layers.Dense(10, activation='relu', input_shape=(input_dim,)),
            tf.keras.layers.Dense(1)
        ])
        ai_model.compile(optimizer='adam', loss='mse')

        # For demo purposes, we ignore 'circuit' and let hybrid_simulate work with the provided state.
        fidelity = quantum_simulation.hybrid_simulate(None, operator, ai_model, quantum_state)
        return jsonify({"status": "success", "fidelity": fidelity})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

if __name__ == '__main__':
    # Consider replacing debug=True with proper production logging and SSL/TLS configuration.
    app.run(debug=True, host='0.0.0.0', port=8000)
