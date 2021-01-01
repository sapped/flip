import requests
import json

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