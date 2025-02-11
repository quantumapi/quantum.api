from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field
from typing import List, Dict, Any
import logging
import os
from prometheus_client import start_http_server, Counter, Histogram
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from fastapi.middlewares.import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import jwt
from datetime import datetime, timedelta
from quantum_api.quantum_circuit import create_error_corrected_circuit
from quantum_api.quantum_simulation import simulate_quantum_circuit
from quantum_api.ai_integration import ai_optimize_quantum_circuit
from quantum_api.security import encrypt_data, decrypt_data
from quantum_api.blockchain_integration import log_to_blockchain, get_blockchain_log
from quantum_api.utils import setup_logging
