from flask import Flask, request, jsonify
import quantum_api.quantum_circuit as qc
import quantum_api.quantum_simulation as qs
import quantum_api.ai_integration as ai_integration

app = Flask(__name__)

@app.route('/create_dynamic_circuit', methods=['POST'])
def create_dynamic_circuit():
    data = request.get_json()
    gates = data['gates']
    qubits = data['qubits']
    result = qc.create_dynamic_quantum_circuit(gates, qubits)
    return jsonify(result)

@app.route('/simulate_with_ai', methods=['POST'])
def simulate_with_ai():
    data = request.get_json()
    quantum_state = data['quantum_state']
    operator = data['operator']
    ai_model = ai_integration.load_model(data['ai_model'])
    result = qs.simulate_quantum_state_with_ai(quantum_state, operator, ai_model)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
