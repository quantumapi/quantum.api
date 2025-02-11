
# Use a multi-stage build for a slim, production-ready image

# Stage 1: Build environment
FROM python:3.10-slim AS builder
WORKDIR /app
COPY . /app
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Stage 2: Final runtime image
FROM python:3.10-slim
WORKDIR /app
COPY --from=builder /app /app
EXPOSE 8000
CMD ["python", "start_server.py"]
