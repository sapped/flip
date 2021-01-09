import requests

from sessionstate import _get_full_session
from config import API_URL

class User():
    def __init__(self):
        self.resource = f'{API_URL}/user'
        self.current_username = _get_active_user()
        self.db_user = self.get_db_user()


    def get_db_user(self):
        json = {
            'username': self.current_username
        }
        
        res = requests.get(f'{self.resource}/username', json=json)
        return res.json()

def _get_active_user():
    session = _get_full_session()
    user = session.ws.request.headers['X-Forwarded-User']
    return user