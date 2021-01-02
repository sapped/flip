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

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR,'.env'))

app = FastAPI(
    openapi_url="/api/v1/openapi.json",
    root_path='/api/v1'
)

app.add_middleware(
    DBSessionMiddleware,
    db_url=os.environ['DATABASE_URL'])


# ---------- MANAGE GOALS ---------- #

# create a new goal
@app.post('/goals/', response_model=schema.Goal)
def create_goal(goal: schema.Goal):
    
    db_goal = models.Goal(
        goal = goal.goal,
        has_amount = goal.has_amount,
        date_created = dt.datetime.now(),
    )
    db.session.add(db_goal)
    db.session.commit()
    return db_goal

# read all goals
@app.get('/goals/')
def read_goals():
    db_goals = db.session.query(models.Goal).all()
    return db_goals

# delete a goal
@app.post("/goals/delete/{id}", response_model=schema.Goal)
def delete_goal(id: int):
    db_goal = db.session.query(models.Goal).filter(models.Goal.id == id).first()
    db.session.delete(db_goal)
    db.session.commit()
    return db_goal

# --------- MANAGE ENTRIES --------- #

# create an entry
@app.post("/entry/", response_model=schema.Entry)
def create_entryr(entry: schema.Entry):
    db_entry = models.Entry(
        goal_id=entry.goal_id,
        date=entry.date,
        tracked=entry.tracked,
        amount=entry.amount,)
    db.session.add(db_entry)
    db.session.commit()
    return db_entry

# update an existing entry
@app.post("/entry/update/{id}", response_model=schema.Entry)
def update_entry(id: int, entry: schema.Entry):
    db_entry = db.session.query(models.Entry).filter(models.Entry.id == id).first()
    db_entry.goal_id = entry.goal_id
    db_entry.date = entry.date
    db_entry.tracked = entry.tracked
    db_entry.amount = entry.amount
    db.session.commit()
    return db_entry

# delete an existing entry
@app.post("/entry/delete/{id}", response_model=schema.Entry)
def delete_entry(id: int):
    db_entry = db.session.query(models.Entry).filter(models.Entry.id == id).first()
    db.session.delete(db_entry)
    db.session.commit()
    return db_entry

# get entries
@app.get('/entries/')
def get_entries(count: int = 7):
    db_entries = db.session.query(models.Entry).limit(count).all()
    return db_entries

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)