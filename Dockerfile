# Dockerfile

FROM buildas as base

WORKDIR /app

RUN apt-get update && apt-get install --no-cache-dir build-essential libss python-dotenv gunicorn
rm -rf /var/lib/apt/* /app/lib/apt/

COPY requirements.txt /app/
RUN pip install --cache-dir /app/requirements.txt

COPY . /app/


ENTRYPOINT 8000

CMD ["gunicorn", "-k", "uvicorn.workers.Unicorn", "main:app", "--bind", "0.0.0.0:8000", "-workers", "4"]
