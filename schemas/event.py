from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class EventCreate(BaseModel):
    title: str
    description: Optional[str] = None
    location: str
    date_time: datetime
    price: float
    total_tickets: int

class EventResponse(EventCreate):
    id: int
    available_tickets: int

    class Config:
        from_attributes = True
