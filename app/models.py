from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Quote(Base):
    __tablename__ = "quotes"

    id = Column(Integer, primary_key=True, index=True)
    quote = Column(Text, unique=True, nullable=False)
    author = Column(Text, nullable=False)