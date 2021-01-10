import time
from typing import List

from fastapi import APIRouter, HTTPException
from fastapi_sqlalchemy import db

from . import model
from . import schema

router = APIRouter(
    prefix='/tracker',
    tags=['Tracker']
)

@router.get('/entry_type', response_model=List[schema.Entry_Type])
def get_entry_types():
    db_entry_types = db.session.query(model.Entry_Type).all()
    return db_entry_types

@router.post('/entry_type', response_model=schema.Entry_Type)
def create_entry_type(entry_type: schema.Entry_Type):
    db_entry_type = model.Entry_Type(
        entry_type = entry_type.entry_type,
        has_description = entry_type.has_description,
        has_amount = entry_type.has_amount,
        created_at = time.time(),
        user_id = entry_type.user_id,
    )
    db.session.add(db_entry_type)
    db.session.commit()

    return db_entry_type