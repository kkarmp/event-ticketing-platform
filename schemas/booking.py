from pydantic import BaseModel
from datetime import datetime

class BookingCreate(BaseModel):
    event_id: int
    tickets_count: int

class BookingResponse(BaseModel):
    id: int
    user_id: int
    event_id: int
    tickets_count: int
    total_price: float
    created_at: datetime

    class Config:
        from_attributes = True
