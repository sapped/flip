import time
import requests
from datetime import datetime

import pandas as pd

from sessionstate import _get_full_session
from config import API_URL

class Tracker():
    def __init__(self, hours_back=24):
        self.resource = f'{API_URL}/tracker'
        self.existing_types = self.existing_types()
        self.existing_entries = self.existing_entries(hours_back)

    def existing_entries(self,hours_back):
        res = requests.get(f'{self.resource}/entry')
        cutoff_time = time.time()
        cutoff_time -= 24*60*60
        LD = res.json()
        if LD == []:
            return pd.DataFrame()
        else:
            v = {k: [dic[k] for dic in LD] for k in LD[0]}
            df = pd.DataFrame(v)
            df = df[df['created_at']>=cutoff_time]
            df['created_at'] = df['created_at'].apply(datetime.fromtimestamp)
            return df.set_index('id')

    def existing_types(self):
        res = requests.get(f'{self.resource}/entry_type')
        LD = res.json()
        if LD == []:
            return pd.DataFrame()
        else:
            v = {k: [dic[k] for dic in LD] for k in LD[0]}
            df = pd.DataFrame(v)
            return df.set_index('entry_type')
    
    def create_entry(self, json):
        res = requests.post(f'{self.resource}/entry', json=json)
        LD = res.json()
        return LD

    def create_type(self, entry_type, has_description, has_amount, user_id):
        json = {
            'entry_type': entry_type,
            'has_description': has_description,
            'has_amount': has_amount,
            'user_id': user_id,
        }
        res = requests.post(f'{self.resource}/entry_type', json=json)
        return res.json()

def _get_active_user():
    session = _get_full_session()
    user = session.ws.request.headers['X-Forwarded-User']
    return user