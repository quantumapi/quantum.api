import os
import logging
from flask import Flask, request, jsonify
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')
logger = logging.getLogger(__name__)

# Import modules from quantum_api package
from quantum_api import quantum_circuit, quantum_simulation, ai_integration, blockchain_integration

app = Flask(__name__)

@app.route('/create_circuit', methods=['POST'])
def create_circuit():
    try:
        data = request.get_json(force=True)
        gates = data.get('gates')
        qubits = data.get('qubits')
        if not gates or not qubits:
            return jsonify({"error": "Missing required parameters: 'gates' and 'qubits'"}), 400

        # Create a dynamic quantum circuit based on provided gate sequence
        circuit = quantum_circuit.create_dynamic_quantum_circuit(gates, qubits)
        # Apply advanced error correction (placeholder for future production‑grade QEC)
        circuit = quantum_circuit.apply_surface_code(circuit)
        # Log the operation for audit purposes on the blockchain
        blockchain_integration.log_operation("create_circuit", data)
        return jsonify({"status": "success", "circuit": circuit.qasm()})
    except Exception as e:
        logger.exception("Error creating circuit")
        return jsonify({"error": str(e)}), 500

@app.route('/simulate', methods=['POST'])
def simulate():
    try:
        data = request.get_json(force=True)
        quantum_state = data.get('quantum_state')
        operator = data.get('operator')
        if quantum_state is None or operator is None:
            return jsonify({"error": "Missing 'quantum_state' or 'operator'"}), 400

        result = quantum_simulation.hybrid_simulate(
            quantum_state=quantum_state,
            operator=operator,
            ai_model=ai_integration.load_model(data.get('ai_model', 'default'))
        )
        blockchain_integration.log_operation("simulate", data)
        return jsonify({"status": "success", "result": result})
    except Exception as e:
        logger.exception("Simulation error")
        return jsonify({"error": str(e)}), 500

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json(force=True)
        payload = data.get('data')
        model_name = data.get('model')
        if payload is None or model_name is None:
            return jsonify({"error": "Missing 'data' or 'model' parameters"}), 400

        ai_model = ai_integration.load_model(model_name)
        # Use a dedicated function for prediction (can be integrated into ai_integration)
        prediction = ai_integration.ai_predict(payload, ai_model)
        blockchain_integration.log_operation("predict", data)
        return jsonify({"status": "success", "prediction": prediction})
    except Exception as e:
        logger.exception("Prediction error")
        return jsonify({"error": str(e)}), 500

@app.route('/communicate', methods=['POST'])
def communicate():
    try:
        data = request.get_json(force=True)
        message = data.get('data')
        destination = data.get('destination')
        if not message or not destination:
            return jsonify({"error": "Missing 'data' or 'destination' parameters"}), 400

        # Placeholder for interdimensional communication logic
        # For now, simply log and return success
        blockchain_integration.log_operation("communicate", data)
        return jsonify({"status": "success", "message": "Data transmitted successfully to " + destination})
    except Exception as e:
        logger.exception("Communication error")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.getenv("PORT", "8000"))
    debug_mode = os.getenv("DEBUG", "False").lower() == "true"
    app.run(host='0.0.0.0', port=port, debug=debug_mode)
