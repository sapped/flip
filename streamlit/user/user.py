import requests

import streamlit as st

from sessionstate import _get_full_session
from config import API_URL

class User():
    def __init__(self):
        self.resource = f'{API_URL}/user'
        self.current_username = self.get_active_user()
        self.db_user = self.get_db_user()


    def get_db_user(self):
        res = requests.get(f'{self.resource}/{self.current_username}')
        return res.json()
f
    def get_active_user(self):
        session = _get_full_session()
        try:
            user = session.ws.request.headers['X-Forwarded-User']
        except KeyError:
            user = 'ed'
            # user_list = requests.get(f'{self.resource}')
            # st.write(user_list)
            # user = st.selectbox(options=user_list['name'])

        return user