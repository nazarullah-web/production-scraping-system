from sqlalchemy.orm import Session

from app.models import Quote
from app.scraper.quotes import scrape_quotes


def ingest_quotes(db: Session) -> dict:
    """
    Scrape quotes and save new records to the database.
    """

    quotes = scrape_quotes()

    inserted = 0

    for item in quotes:

        exists = (
            db.query(Quote)
            .filter(Quote.quote == item["quote"])
            .first()
        )

        if exists:
            continue

        db.add(
            Quote(
                quote=item["quote"],
                author=item["author"]
            )
        )

        inserted += 1

    db.commit()

    return {
        "status": "success",
        "inserted": inserted,
        "total_scraped": len(quotes)
    }