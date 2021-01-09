from typing import List

import uvicorn
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

import os
import datetime as dt
from fastapi_sqlalchemy import DBSessionMiddleware
from fastapi_sqlalchemy import db
from dotenv import load_dotenv

import models
import schema

from user import router as user_router

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR,'.env'))

app = FastAPI(
    openapi_url="/api/v1/openapi.json",
    root_path='/api/v1'
)

app.add_middleware(
    DBSessionMiddleware,
    db_url=os.environ['DATABASE_URL'])

app.include_router(user_router.router)


# ---------- MANAGE GOALS ---------- #

# CREATE new goal
@app.post('/goals/', response_model=schema.Goal)
def create_goal(goal: schema.Goal):
    
    db_goal = models.Goal(
        goal = goal.goal,
        has_amount = goal.has_amount,
        date_created = goal.date_created,
    )
    db.session.add(db_goal)
    db.session.commit()
    return db_goal

# READ all goals
@app.get('/goals/')
def read_goals():
    db_goals = db.session.query(models.Goal).all()
    return db_goals

# UPDATE na

# DELETE a goal
@app.post("/goals/delete/{id}", response_model=schema.Goal)
def delete_goal(id: int):
    db_goal = db.session.query(models.Goal).filter(models.Goal.id == id).first()
    db.session.delete(db_goal)
    db.session.commit()
    return db_goal

# --------- MANAGE ENTRIES --------- #

# CREATE an entry
@app.post("/entries/", response_model=List[schema.Entry])
def create_entry(entries: List[schema.Entry]):
    
    db_entries = []
    for entry in entries:
        db_entry = models.Entry(
            goal_id=entry.goal_id,
            date=entry.date,
            tracked=entry.tracked,
            amount=entry.amount,)
        db.session.add(db_entry)
        db.session.commit()
        db_entries.append(db_entry)
    return db_entries

# READ entries
@app.get('/entries/')
def get_entries(count: int = 365):
    db_entries = db.session.query(models.Entry).limit(count).all()
    return db_entries

# UPDATE na

# DELETE an existing entry
@app.post("/entries/delete/", response_model=List[schema.Entry])
def delete_entry(entries: List[int]):
    print('-------------------------------')
    print(entries)
    print('-------------------------------')

    db_entries = []
    for id in entries:
        db_entry = db.session.query(models.Entry).filter(models.Entry.id == id).first()
        db.session.delete(db_entry)
        db.session.commit()
        db_entries.append(db_entry)
    return db_entries

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)