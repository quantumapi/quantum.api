# tests/test_quantum_api.py
import pytest
from fastapi.testclient import TestClient
from quantum_api.main import app

client = TestClient(app)

def test_compute_endpoint():
    # Test with a simple array of floats
    payload = {"data": [0.0, 1.0, 2.0]}
    response = client.post("/compute", json=payload)
    assert response.status_code == 200
    json_response = response.json()
    assert "result" in json_response
    # Optionally, add further checks on the structure or decrypt the result if needed
