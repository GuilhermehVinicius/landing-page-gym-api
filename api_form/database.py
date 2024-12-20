import os
from api_form.settings import Settings
from sqlmodel import Session, SQLModel, create_engine


engine = create_engine(Settings().DATABASE_URL)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session