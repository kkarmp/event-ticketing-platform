from repositories.booking_repository import BookingRepository
from repositories.event_repository import EventRepository
from schemas.booking import BookingCreate
from models.booking import Booking
from fastapi import HTTPException

class BookingService:
    def __init__(self, booking_repo: BookingRepository, event_repo: EventRepository):
        self.booking_repo = booking_repo
        self.event_repo = event_repo

    def create_booking(self, user_id: int, data: BookingCreate):
        event = self.event_repo.get_by_id(data.event_id)
        if not event:
            raise HTTPException(status_code=404, detail="Event not found")
        if event.available_tickets < data.tickets_count:
            raise HTTPException(status_code=400, detail="Not enough tickets available")

        total_price = event.price * data.tickets_count
        event.available_tickets -= data.tickets_count
        self.event_repo.update()

        booking = Booking(
            user_id=user_id,
            event_id=data.event_id,
            tickets_count=data.tickets_count,
            total_price=total_price
        )
        return self.booking_repo.create(booking)
