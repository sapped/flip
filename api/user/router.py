import time

from fastapi import APIRouter, HTTPException
from fastapi_sqlalchemy import db

from . import model
from . import schema

router = APIRouter(
    prefix = '/user',
    tags = ['User']
)

@router.get('/username', response_model=schema.User)
def get_or_create_user(user: schema.User):
    db_user = db.session.query(model.User).filter(model.User.id==user.id).first()
    
    # user doesn't exist, create (users managed by htpasswd)
    if db_user is None:
        db_user = model.User(
            username = user.username,
            created_at = time.time()
        )
        db.session.add(db_user)
        db.session.commit()
    
    return db_user