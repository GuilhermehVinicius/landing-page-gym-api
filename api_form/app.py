from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import select, Session
from fastapi.middleware.cors import CORSMiddleware
from api_form.schemas import LeadBase, Lead, LeadPublic, LeadCreate, LeadUpdate
from api_form.database import create_db_and_tables, get_session

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:5500"

]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.post("/leads/", response_model=LeadPublic)
def create_hero(lead: LeadCreate, session: Session = Depends(get_session)):
    db_hero = Lead.model_validate(lead)
    session.add(db_hero)
    session.commit()
    session.refresh(db_hero)
    return db_hero