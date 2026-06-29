from fastapi import FastAPI

from app.database import engine
from app.models import Base
from app.api.quotes import router as quotes_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Production Scraping System",
    version="0.1.0"
)

app.include_router(quotes_router)


@app.get("/")
def root():
    return {
        "message": "Production Scraping System API"
    }