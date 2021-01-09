from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    id: Optional[int]
    username: str
    created_at: Optional[float]

    class Config:
        orm_mode=True