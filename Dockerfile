# Stage 1: Builder
FROM python:3.10-slim as builder
WORKDIR /app
# Install build dependencies if necessary (e.g., gcc, libffi-dev, etc.)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Stage 2: Runtime
FROM python:3.10-slim
WORKDIR /app
# Copy installed packages and source code from builder
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=builder /app /app
# Create non-root user and switch to it
RUN adduser --disabled-password quantum
USER quantum
EXPOSE 8000
CMD ["python", "start_server.py"]
