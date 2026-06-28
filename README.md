# Production Scraping System

A production-style web scraping system built using Python, FastAPI, and SQLAlchemy.

## Features

- Web scraping using BeautifulSoup
- SQLAlchemy ORM
- FastAPI API
- ETL ingestion pipeline
- Duplicate prevention
- Clean architecture

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- BeautifulSoup
- Requests
- SQLite

## Project Structure

app/
api/
scraper/
services/

## Run

pip install -r requirements.txt

uvicorn app.main:app --reload

## License

MIT