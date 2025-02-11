# Base image for quantum simulation
FROM python:3.8-slim as base

# Python dependencies for quantum and AI packages
FROM python:3.8-slim as builder

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

# Final image
FROM python:3.8-slim

WORKDIR /app

COPY --from=builder /app /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["python", "start_server.py"]
