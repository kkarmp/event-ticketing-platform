from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from schemas.booking import BookingCreate, BookingResponse
from repositories.booking_repository import BookingRepository
from repositories.event_repository import EventRepository
from services.booking_service import BookingService

router = APIRouter(prefix="/bookings", tags=["Bookings"])

@router.post("/", response_model=BookingResponse)
def create_booking(booking_data: BookingCreate, db: Session = Depends(get_db)):
    service = BookingService(BookingRepository(db), EventRepository(db))
    return service.create_booking(user_id=1, data=booking_data)
