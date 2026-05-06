FROM python:3.11-slim

WORKDIR /app

COPY src/requirements.txt .

RUN pip install -r requirements.txt

COPY src/. .

EXPOSE 80

CMD ["python", "app.py"]
