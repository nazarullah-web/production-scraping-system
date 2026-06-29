from fastapi import FastAPI

from app.database import engine
from app.models import Base
from app.api.quotes import router as quotes_router
from app.core.settings import settings

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)

app.include_router(quotes_router)


@app.get("/")
def root():
    return {
        "message": "Production Scraping System API"
    }