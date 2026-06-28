from app.database import SessionLocal, engine
from app.models import Base
from app.services.ingestion import ingest_quotes

Base.metadata.create_all(bind=engine)


def main():

    db = SessionLocal()

    try:
        result = ingest_quotes(db)
        print(result)

    finally:
        db.close()


if __name__ == "__main__":
    main()