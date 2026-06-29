from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.quote import QuoteResponse
from app.services.ingestion import ingest_quotes

from app.database import get_db
from app.models import Quote

from app.schemas.quote import (
    QuoteResponse,
    ScrapeResponse,
)

router = APIRouter(
    prefix="/quotes",
    tags=["Quotes"]
)


@router.get(
    "/",
    response_model=list[QuoteResponse]
)
def get_quotes(db: Session = Depends(get_db)):

    return db.query(Quote).all()

@router.post(
    "/scrape",
    response_model=ScrapeResponse
)
def scrape_and_save(
    db: Session = Depends(get_db)
):
    return ingest_quotes(db)