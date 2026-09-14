from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from db.database import Base

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    description = Column(String, nullable=True)
    location = Column(String, nullable=False)
    date_time = Column(DateTime, default=datetime.utcnow, nullable=False)
    price = Column(Float, nullable=False)
    total_tickets = Column(Integer, nullable=False)
    available_tickets = Column(Integer, nullable=False)
