import time

from fastapi import APIRouter, HTTPException
from fastapi_sqlalchemy import db

from . import model
from . import schema

router = APIRouter(
    prefix='/tracker',
    tags=['Tracker']
)

@router.get('/entry_type', response_model=schema.Entry_Type)
def get_entry_types():
    