import uvicorn
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

import os
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

# arbitrary user resource I built when following a tutorial - not used in streamlit CRUD example

# create a tracker entry
@app.post("/tracker/", response_model=schema.Tracker)
def create_tracker(tracker: schema.Tracker):
    db_tracker = models.Tracker(
        date=tracker.date,
        crossfit=tracker.crossfit,
        gowod=tracker.gowod,
        yoga=tracker.yoga,
        weight=tracker.weight,
        calories=tracker.calories,)
    db.session.add(db_tracker)
    db.session.commit()
    return db_tracker

# update an existing tracker
@app.post("/tracker/update/{id}", response_model=schema.Tracker)
def update_tracker(id: int, tracker: schema.Tracker):
    db_tracker = db.session.query(models.Tracker).filter(models.Tracker.id == id).first()
    db_tracker.crossfit = tracker.crossfit
    db_tracker.gowod = tracker.gowod
    db_tracker.yoga = tracker.yoga
    db_tracker.weight = tracker.weight
    db_tracker.calories = tracker.calories
    db.session.commit()
    return db_tracker

# delete an existing tracker
@app.post("/tracker/delete/{id}", response_model=schema.Tracker)
def delete_tracker(id: int):
    db_tracker = db.session.query(models.Tracker).filter(models.Tracker.id == id).first()
    db.session.delete(db_tracker)
    db.session.commit()
    return db_tracker

# get all trackers
@app.get('/trackers/')
def get_trackers():
    db_trackers = db.session.query(models.Tracker).all()
    return db_trackers

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)