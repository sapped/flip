from pydantic import BaseModel
from datetime import datetime

class Goal(BaseModel):
    goal: str
    has_amount: bool

    class Config:
        orm_mode = True

class Entry(BaseModel):
    goal_id: int
    date: datetime
    tracked: bool
    amount: float

    class Config:
        orm_mode = True