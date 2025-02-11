# Quantum.API Documentation

Welcome to the Quantum.API documentation. This guide provides detailed information on how to use the various endpoints provided by the Quantum.API platform.

## Table of Contents

- [Endpoints](#endpoints)
  - [Create Quantum Circuit](#create-quantum-circuit)
  - [Simulate Quantum Circuit](#simulate-quantum-circuit)
  - [Optimize Quantum Circuit](#optimize-quantum-circuit)
  - [Encrypt Data](#encrypt-data)
  - [Decrypt Data](#decrypt-data)
  - [Log to Blockchain](#log-to-blockchain)
  - [Get Blockchain Log](#get-blockchain-log)

## Endpoints

### Create Quantum Circuit

**Endpoint**: `POST /create_circuit`

**Description**: Create a quantum circuit based on a sequence of gate instructions.

**Request Body**:
```json
{
  "gate_sequence": [
    {
      "type": "H",
      "target": 0
    }
  ],
  "num_qubits": 2
}
```

**Response**:
```json
{
  "circuit": "OPENQASM 2.0; ..."
}
```

### Simulate Quantum Circuit

**Endpoint**: `POST /simulate_circuit`

**Description**: Simulate a quantum circuit based on a sequence of gate instructions.

**Request Body**:
```json
{
  "gate_sequence": [
    {
      "type": "H",
      "target": 0
    }
  ],
  "num_qubits": 2
}
```

**Response**:
```json
{
  "statevector": [0.7071067811865475, 0, 0, 0.7071067811865475]
}
```

### Optimize Quantum Circuit

**Endpoint**: `POST /optimize_circuit`

**Description**: Optimize a quantum circuit using an AI model.

**Request Body**:
```json
{
  "gate_sequence": [
    {
      "type": "H",
      "target": 0
    }
  ],
  "num_qubits": 2
}
```

**Response**:
```json
{
  "optimized_circuit": "OPENQASM 2.0; ..."
}
```

### Encrypt Data

**Endpoint**: `POST /encrypt`

**Description**: Encrypt data using Fernet symmetric encryption.

**Request Body**:
```json
{
  "data": "sensitive information"
}
```

**Response**:
```json
{
  "encrypted_data": "gAAAAABc..."
}
```

### Decrypt Data

**Endpoint**: `POST /decrypt`

**Description**: Decrypt data using Fernet symmetric encryption.

**Request Body**:
```json
{
  "data": "gAAAAABc..."
}
```

**Response**:
```json
{
  "decrypted_data": "sensitive information"
}
```

### Log to Blockchain

**Endpoint**: `POST /log_to_blockchain`

**Description**: Log an operation to the blockchain.

**Request Body**:
```json
{
  "operation": "create_circuit",
  "details": {
    "gate_sequence": [
      {
        "type": "H",
        "target": 0
      }
    ],
    "num_qubits": 2
  }
}
```

**Response**:
```json
{
  "tx_hash": "0x1234567890abcdef..."
}
```

### Get Blockchain Log

**Endpoint**: `GET /get_blockchain_log/{tx_hash}`

**Description**: Retrieve a log entry from the blockchain.

**Path Parameters**:
- `tx_hash`: The transaction hash of the log entry to retrieve.

**Response**:
```json
{
  "log": {
    "operation": "create_circuit",
    "details": {
      "gate_sequence": [
        {
          "type": "H",
          "target": 0
        }
      ],
      "num_qubits": 2
    }
  }
}
```

## Additional Information

For more detailed information on the API, including request and response schemas, you can visit the interactive API documentation at `http://localhost:8000/docs`.

Thank you for using Quantum.API!
