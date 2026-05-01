FROM python:3.11-slim

WORKDIR /app

COPY src/app.py .

RUN pip install azure-identity azure-storage-blob

CMD ["python", "app.py"]