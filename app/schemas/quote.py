from pydantic import BaseModel, ConfigDict


class QuoteResponse(BaseModel):
    id: int
    quote: str
    author: str

    model_config = ConfigDict(from_attributes=True)
    
class ScrapeResponse(BaseModel):
    status: str
    inserted: int
    total_scraped: int