from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Float, Date

Base = declarative_base()

class ExchangeRate(Base):
    __tablename__ = "exchange_rates"

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    currency_code = Column(String(3))
    currency_name = Column(String(40))
    currency_rate = Column(Float)

