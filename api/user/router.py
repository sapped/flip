import time
from typing import List

from fastapi import APIRouter, HTTPException
from fastapi_sqlalchemy import db

from . import model
from . import schema

router = APIRouter(
    prefix = '/user',
    tags = ['User']
)

@router.get('/', response_model=List[schema.User])
def get_users():
    db_users = db.session.query(model.User).all()
    return db_users

@router.get('/{username}', response_model=schema.User)
def get_or_create_user(username: str):
    db_user = db.session.query(model.User).filter(model.User.username==username).one_or_none()
    # user doesn't exist, create (users managed by htpasswd)
    if db_user is None:
        db_user = model.User(
            username = user.username,
            created_at = time.time()
        )
        db.session.add(db_user)
        db.session.commit()
    
    return db_user