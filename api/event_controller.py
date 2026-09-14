from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from db.database import get_db
from schemas.event import EventCreate, EventResponse
from repositories.event_repository import EventRepository
from services.event_service import EventService

router = APIRouter(prefix="/events", tags=["Events"])

@router.get("/", response_model=List[EventResponse])
def list_events(db: Session = Depends(get_db)):
    service = EventService(EventRepository(db))
    return service.get_all()

@router.post("/", response_model=EventResponse)
def create_event(event_data: EventCreate, db: Session = Depends(get_db)):
    service = EventService(EventRepository(db))
    return service.create(event_data)
