from fastapi import FastAPI

from app.api.routes import router as movie_router

app = FastAPI(title="Movie Similarity API")

app.include_router(movie_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
