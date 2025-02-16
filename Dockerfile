FROM python:3.9-slim

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .
COPY ./app ./app

EXPOSE 8000

CMD ["python", "main.py"]