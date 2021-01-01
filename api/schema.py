from pydantic import BaseModel
from datetime import datetime

class Tracker(BaseModel):
    date: datetime
    crossfit: bool
    gowod: bool
    yoga: bool
    weight: float
    calories: int

    class Config:
        orm_mode = True