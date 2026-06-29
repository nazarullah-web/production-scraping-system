from fastapi import FastAPI

from app.api.quotes import router as quotes_router
from app.core.logging import logger
from app.core.settings import settings
from app.database import engine
from app.models import Base

# Membuat tabel database
Base.metadata.create_all(bind=engine)

# Membuat aplikasi FastAPI
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)

# Event startup
@app.on_event("startup")
def startup():
    logger.info("Application started.")

# Register router
app.include_router(quotes_router)

# Root endpoint
@app.get("/")
def root():
    return {
        "message": "Production Scraping System API"
    }