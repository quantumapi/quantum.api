# main.py
import uvicorn
from fastapi import FastAPI
from quantum_api.routers import quantum_router
from quantum_api.config import settings
from prometheus_client import start_http_server
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter

app = FastAPI(
    title="Quantum.API",
    description="A platform uniting quantum computing, AI-enhanced simulations, and interdimensional communication.",
    version="2.0.0",
)

app.include_router(quantum_router)

# Start Prometheus metrics server
start_http_server(8001)

# Set up OpenTelemetry tracing
trace.set_tracer_provider(TracerProvider())
span_exporter = OTLPSpanExporter(endpoint="http://localhost:4317")
span_processor = BatchSpanProcessor(span_exporter)
trace.get_tracer_provider().add_span_processor(span_processor)

if __name__ == "__main__":
    uvicorn.run(app, host=settings.HOST, port=settings.PORT)
