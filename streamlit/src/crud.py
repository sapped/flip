import requests
import json

import pandas as pd

from config import API_URL

class Goal():

    def __init__(self):
        self.resource = f'{API_URL}/goals/'
        self.existing_goals = self.read_goals()

    def read_goals(self):
        res = requests.get(self.resource)
        df = pd.read_json(res.text)
        return df.set_index('id')

    def create_goal(self, goal):
        url = f'{API_URL}/goals/'
        res = requests.post(url, json=goal)
        return json.loads(res.text)

    def delete_goal(self, id):
        url = f'{API_URL}/goals/delete/{id}'
        res = requests.post(url)
        return json.loads(res.text)

class Entry():

    def read_entries():
        return 'BITCH'

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