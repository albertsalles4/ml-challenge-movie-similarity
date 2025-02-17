# ML Challenge – Movie Similarity Model

This is a challenge to compare text embeddings. The tasks are the following:

1. Research and align on the best similarity approach.
2. Design and deploy a modular and scalable infrastructure for the model.
3. Build and showcase a demo of the solution.

## Getting Started

### Prerequisites

```bash
python -m venv venv # Optional: create a virtual environment
source venv/bin/activate # Activate the virtual environment
pip install -r requirements.txt
```

### Running the app

The app is a FastAPI application. You can run it with the following command:

```bash
python main.py
```

A Swagger UI is available at http://localhost:8000/docs.

Additionally, you can run the app with Docker:

```bash
docker build -t movie-similarity-api .
docker run -p 8000:8000 movie-similarity-api
```

### Frontend

The frontend is a Streamlit application. You can run it with the following command:

```bash
streamlit run frontend/main.py
```

Additionally, you can run the frontend with Docker:

```bash
docker build -f frontend.Dockerfile -t movie-similarity-frontend .
docker run -p 8501:8501 movie-similarity-frontend
```

### Docker Compose

You can run the entire application with Docker Compose:

```bash
docker-compose up
```

## Author

[Albert Sallés](https://www.linkedin.com/in/albert-salles/) – [github.com/albertsalles4](https://github.com/albertsalles4)