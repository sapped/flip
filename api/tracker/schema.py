from typing import Optional
from pydantic import BaseModel

class Entry_Type(BaseModel):
    entry_type: str
    has_description: bool
    has_amount: bool
    created_at: Optional[float]
    user_id: int

    class Config:
        orm_mode=True

class Entry(BaseModel):
    id: Optional[int]
    entry_type: str
    description: str
    amount: float
    created_at: Optional[float]
    user_id: int

    class Config:
        orm_mode=True