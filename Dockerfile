# Dockerfile
# Use a multi-stage build to keep the final image small
FROM python:3.8-slim AS builder

WORKDIR /app
COPY . /app

# Install production dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Final stage: copy only the necessary files
FROM python:3.8-slim

WORKDIR /app

# Copy the installed dependencies from the builder stage
COPY --from=builder /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages

# Copy the application code
COPY . /app

# Expose the port
EXPOSE 8000

# Load environment variables from .env file
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Create a non-root user to run the application
RUN useradd -m appuser
USER appuser

# Run the application using uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
