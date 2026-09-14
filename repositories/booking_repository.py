from sqlalchemy.orm import Session
from models.booking import Booking

class BookingRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, booking: Booking):
        self.db.add(booking)
        self.db.commit()
        self.db.refresh(booking)
        return booking

    def get_by_user(self, user_id: int):
        return self.db.query(Booking).filter(Booking.user_id == user_id).all()
