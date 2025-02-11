# quantum_api/Dockerfile
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire codebase
COPY . .

# Expose port 8000 and run the app
EXPOSE 8000
CMD ["uvicorn", "quantum_api.quantum_api:app", "--host", "0.0.0.0", "--port", "8000"]
