from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from db.database import engine, Base
from api import auth_controller, event_controller, booking_controller

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Event Ticketing Platform",
    description="Final Project for Coding Factory 10 - AUEB",
    version="1.0.0"
)

app.include_router(auth_controller.router)
app.include_router(event_controller.router)
app.include_router(booking_controller.router)

app.mount("/static", StaticFiles(directory="static", html=True), name="static")

@app.get("/")
def root():
    return {"message": "Welcome to Event Ticketing API. Visit /docs for Swagger UI or /static for Frontend."}
