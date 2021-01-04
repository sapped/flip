# stdlib imports
import requests
import json

# library imports
import streamlit as st
import pandas as pd

# local imports
from config import API_URL

class Goal():

    def __init__(self):
        self.resource = f'{API_URL}/goals/'
        self.existing_goals = self.read_goals()

    def read_goals(self):
        res = requests.get(self.resource)
        df = pd.read_json(res.text, convert_dates=False)
        try:
            df.set_index('id', inplace=True)
            return df
        except KeyError:
            return df

    def create_goal(self, goal):
        res = requests.post(self.resource, json=goal)
        return json.loads(res.text)

    def delete_goal(self, id):
        url = f'{self.resource}delete/{id}'
        res = requests.post(url)
        return json.loads(res.text)

class Entry():

    def __init__(self):
        # list of dates, least to most recent
        self.resource = f'{API_URL}/entries/'
        self.existing_entries = self.read_entries()

    def read_entries(self):
        res = requests.get(self.resource)
        df = pd.read_json(res.text, convert_dates=False)
        try:
            df.set_index('id', inplace=True)
            return df
        except KeyError:
            return df
    
    def create_entry(self, entry):
        res = requests.post(self.resource, json=entry)
        return json.loads(res.text)
    
    def delete_entry(self, entries):
        res = requests.post(f'{self.resource}delete/', json=entries)
        return json.loads(res.text)


class Tracker():

    def read_tracker():
        url = f'{API_URL}/trackers/'
        res = requests.get(url)
        df = pd.read_json(res.text)
        return df.set_index('id')

    def submit_tracker(tracker):
        url = f'{API_URL}/tracker/'
        res = requests.post(url, json=tracker)
        return json.loads(res.text)

    def delete_tracker(id):
        url = f'{API_URL}/tracker/delete/{id}'
        res = requests.post(url)
        return json.loads(res.text)

    def update_tracker(tracker, id):
        url = f'{API_URL}/tracker/update/{id}'
        res = requests.post(url, json=tracker)
        return json.loads(res.text)