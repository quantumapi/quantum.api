# test_app.py
import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_simulation_endpoint():
    response = client.get("/simulate?param=0.5")
    assert response.status_code == 200
    data = response.json()
    assert "encrypted_result" in data

def test_decrypt_endpoint():
    # First, simulate and encrypt data
    simulation_response = client.get("/simulate?param=0.5")
    encrypted_result = simulation_response.json()["encrypted_result"]
    # Now, attempt to decrypt it
    decrypt_response = client.get(f"/decrypt?encrypted={encrypted_result}")
    assert decrypt_response.status_code == 200
    data = decrypt_response.json()
    assert "decrypted_result" in data
