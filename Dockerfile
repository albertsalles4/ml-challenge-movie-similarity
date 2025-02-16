FROM python:3.9-slim

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Download NLTK models during build time
RUN python -m nltk.downloader -d /usr/local/nltk_data punkt

COPY main.py .
COPY ./app ./app

EXPOSE 8000

CMD ["python", "main.py"]