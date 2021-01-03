from typing import Optional
from pydantic import BaseModel

class Goal(BaseModel):
    goal: str
    has_amount: bool
    date_created: float

    class Config:
        orm_mode = True

class Entry(BaseModel):
    goal_id: int
    tracked: bool
    amount: Optional[float]
    date: Optional[float]

    class Config:
        orm_mode = True