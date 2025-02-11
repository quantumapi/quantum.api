import os
import logging
from flask import Flask, request, jsonify
from dotenv import load_dotenv

# Load configuration from .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from quantum_api import quantum_circuit, quantum_simulation, ai_integration, blockchain_integration

app = Flask(__name__)

@app.route('/create_dynamic_circuit', methods=['POST'])
def create_dynamic_circuit():
    try:
        data = request.get_json(force=True)
        gates = data.get('gates')
        qubits = data.get('qubits')
        if not gates or not qubits:
            return jsonify({"error": "Missing required parameters"}), 400
        circuit = quantum_circuit.create_dynamic_quantum_circuit(gates, qubits)
        # Optionally, perform advanced error correction
        circuit = quantum_circuit.apply_surface_code(circuit)
        # Log the operation on blockchain for audit
        blockchain_integration.log_operation("create_dynamic_circuit", data)
        return jsonify({"status": "success", "circuit": circuit.qasm()})
    except Exception as e:
        logger.exception("Error creating dynamic circuit")
        return jsonify({"error": str(e)}), 500

@app.route('/simulate_with_ai', methods=['POST'])
def simulate_with_ai():
    try:
        data = request.get_json(force=True)
        quantum_state = data.get('quantum_state')
        operator = data.get('operator')
        ai_model_name = data.get('ai_model')
        if quantum_state is None or operator is None or ai_model_name is None:
            return jsonify({"error": "Missing required parameters"}), 400

        ai_model = ai_integration.load_model(ai_model_name)
        result = quantum_simulation.hybrid_simulate(
            quantum_state=quantum_state,
            operator=operator,
            ai_model=ai_model
        )
        # Log simulation request on blockchain
        blockchain_integration.log_operation("simulate_with_ai", data)
        return jsonify({"status": "success", "result": result})
    except Exception as e:
        logger.exception("Error in simulation with AI")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Configuration from env
    port = int(os.getenv("PORT", 8000))
    debug_mode = os.getenv("DEBUG", "False") == "True"
    app.run(debug=debug_mode, host='0.0.0.0', port=port)
