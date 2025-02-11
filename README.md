# Quantum API Supreme

## Overview

This repository contains a production-ready API bridging quantum computing, secure cryptography, and scalable architectures. The API is built using FastAPI and integrates quantum simulations via Qiskit, ensuring secure data handling with AES-GCM encryption.

## Prerequisites

- Python 3.9+
- Docker
- Node.js (for running the JavaScript server)

## Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/quantum-api-supreme.git
    cd quantum-api-supreme
    ```

2. **Install Python dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Set up environment variables:**

    Create a `.env` file in the root directory with the following content:

    ```env
    # Environment variables for the FastAPI application

    # Encryption settings
    ENCRYPTION_PASSPHRASE=your_supersecret_passphrase
    ENCRYPTION_SALT=your_salt

    # Allowed origins for CORS
    ALLOWED_ORIGIN=*

    # Port for the FastAPI server
    PORT=8000
    ```

4. **Build and run the Docker container:**

    ```bash
    docker build -t quantum-api-supreme .
    docker run -p 8000:8000 quantum-api-supreme
    ```

5. **Run the JavaScript server:**

    ```bash
    npm install
    node src/app.js
    ```

## API Endpoints

- **Simulate Quantum Algorithm:**
  - **Endpoint:** `/simulate`
  - **Method:** `GET`
  - **Query Parameters:**
    - `param` (float): Quantum parameter (must be > 0)
  - **Response:**
    ```json
    {
      "encrypted_result": "base64_encoded_encrypted_result"
    }
    ```

- **Decrypt Simulation Result:**
  - **Endpoint:** `/decrypt`
  - **Method:** `GET`
  - **Query Parameters:**
    - `encrypted` (string): Encrypted result string
  - **Response:**
    ```json
    {
      "decrypted_result": "decrypted_result"
    }
    ```

## Testing

Run the tests using Pytest:

```bash
pytest tests/test_app.py
```

## Contributing

Contributions are welcome! Please read the [CONTRIBUTING.md](CONTRIBUTING.md) file for details on our code of conduct, and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the Qiskit team for providing the quantum computing framework.
- Thanks to the FastAPI team for creating the modern web framework.
- Thanks to the Cryptography team for providing secure encryption libraries.
