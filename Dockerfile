FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    tcpdump \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY honeypot_server.py .
COPY ddos_simulator.py .

CMD ["python", "honeypot_server.py"]  # Default run honeypot
