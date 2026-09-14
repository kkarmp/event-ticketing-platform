from repositories.event_repository import EventRepository
from schemas.event import EventCreate
from models.event import Event

class EventService:
    def __init__(self, repo: EventRepository):
        self.repo = repo

    def get_all(self):
        return self.repo.get_all()

    def create(self, data: EventCreate):
        event = Event(
            title=data.title,
            description=data.description,
            location=data.location,
            date_time=data.date_time,
            price=data.price,
            total_tickets=data.total_tickets,
            available_tickets=data.total_tickets
        )
        return self.repo.create(event)
