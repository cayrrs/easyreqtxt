from pydantic import BaseModel
import sqlalchemy
from sqlalchemy.orm import sessionmaker
import datetime


class User(BaseModel):
    id: int
    name: str
    created_at: datetime.datetime


engine = sqlalchemy.create_engine("sqlite:///test.db")
Session = sessionmaker(bind=engine)
