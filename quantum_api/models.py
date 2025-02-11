# models.py
from pydantic import BaseModel
from typing import List

class QuantumRequest(BaseModel):
    """
    Model for incoming quantum computation requests.
    """
    data: List[float]

class QuantumResponse(BaseModel):
    """
    Model for the API response containing the encrypted computation result.
    """
    result: str
