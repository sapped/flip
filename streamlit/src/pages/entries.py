import time
import datetime as dt

import streamlit as st
import pandas as pd

from src.crud import Goal, Entry
from src.style.charts import line_chart, heatmap

from config import API_URL

PAGE_TITLE = 'Track Performance'

def write():
    st.markdown(f'# {PAGE_TITLE}')

    # initialize crud objects
    entries = Entry()
    goals = Goal()

    # read_entries(entries, goals)
    create_entry(entries, goals)

def read_entries(entries, goals):
    st.markdown('### List Existing Goals')
    st.write(goals.existing_goals)

    st.markdown('### List Existing Entries')
    st.write(entries.existing_entries)

# TBU don't create duplicate entry for the same day
def create_entry(entries, goals):
    st.markdown('### Create New Entry')
    st.write('Select what you have tracked today, certain items may require further detail on amount if checked.')
    
    now = time.time()
    st.write(now)
    try:
        max_entry_date = entries.existing_entries['date'].max()
    except:
        max_entry_date = now

    st.write(now)
    st.write(max_entry_date)

    # prepare the entry dictionary for submission to API
    new_entry = goals.existing_goals.reset_index().sort_values(by=['has_amount'], ascending=False).rename(columns={'id':'goal_id'}).to_dict('records')
    for entry in new_entry:
        goal = entry['goal']
        if entry['has_amount'] == True:
            entry['tracked'] = st.checkbox(label=goal)
            if entry['tracked'] == True:
                entry['amount'] = st.number_input(label=goal)
        else:
            entry['tracked'] = st.checkbox(label=goal)
        # get rid of helpful data not part of submission
        entry['date'] = now
        entry.pop('goal')
        entry.pop('date_created')
        entry.pop('has_amount')

    # create the entry (speak to API)
    create = st.button(label='Create entry')

    if create:
        entry_response = entries.create_entry(new_entry)
        if entry_response is not None:
            create = False  

if __name__=='__main__':
    write()