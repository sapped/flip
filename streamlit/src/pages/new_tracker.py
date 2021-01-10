# stdlib imports

# library imports
import streamlit as st
import pandas as pd

# local imports
from user.user import User
from tracker.tracker import Tracker

PAGE_TITLE = 'Goal Tracking v2'

def write():
    st.markdown(f'# {PAGE_TITLE}')
    
    # initialize models
    user = User()
    user_id = user.db_user['id']
    tracker = Tracker()

    st.markdown('## 1. Choose Goal & Submit Entry')
    submit_entry(tracker, user_id)

    st.markdown('## 2. Review Entries')

    st.markdown('## 3. Create New Entry Type')
    create_type(tracker, user_id)

    footer()

def submit_entry(tracker, user_id):
    choose = st.selectbox(label='Select Entry Type', options=tracker.existing_types.index, index=0)
    row = tracker.existing_types.loc[choose]
    submission = {}
    if row['has_description']:
        submission['description'] = st.text_input(label='Description')
    if row['has_amount']:
        submission['amount'] = st.number_input(label='Amount')
    
    submit = st.button(label='submit')

    submit:
        # need to get variables before dict, then give to dict
        res = tracker.create_entry(
            description=,
            amount=,
            entry_type=,
            user_id=,
        )
        st.write(res)
        create = False



def footer():
        st.write('Feel free to delete or create new goals! \
        Click on the little arrow in the top left \
        to open navigation, then \
        select the appropriate page.')

def create_type(tracker, user_id):

    type_input = {
        'entry_type': st.text_input(label='Entry Type'),
        'has_description': st.checkbox(label='Has Description?'),
        'has_amount': st.checkbox(label='Has Amount?'),
    }
    
    create = st.button(label='create')

    if create:
        
        # need to get variables before dict, then give to dict
        res = tracker.create_type(
            entry_type=type_input['entry_type'],
            has_description=type_input['has_description'],
            has_amount=type_input['has_amount'],
            user_id=user_id,
        )
        st.write(res)
        create = False

if __name__=='__main__':
    write()