import requests
from bs4 import BeautifulSoup

from app.core.logging import logger


def scrape_quotes():
    """
    Scrape quotes from quotes.toscrape.com.

    Returns:
        list[dict]: List of quotes and authors.
    """

    logger.info("Requesting quotes.toscrape.com")

    response = requests.get(
        "https://quotes.toscrape.com",
        timeout=10
    )

    response.raise_for_status()

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    quote_cards = soup.find_all(
        "div",
        class_="quote"
    )

    quotes = []

    for card in quote_cards:

        quote = card.find(
            "span",
            class_="text"
        ).get_text(strip=True)

        author = card.find(
            "small",
            class_="author"
        ).get_text(strip=True)

        quotes.append(
            {
                "quote": quote,
                "author": author
            }
        )

    logger.info(f"Successfully parsed {len(quotes)} quotes.")

    return quotes