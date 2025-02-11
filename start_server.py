import uvicorn
import signal
from quantum_api.config import settings

def shutdown_handler(signal, frame):
    print("Shutting down server gracefully...")
    # Add any cleanup code here if needed
    exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, shutdown_handler)
    signal.signal(signal.SIGTERM, shutdown_handler)

    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG,
        workers=4,
    )
