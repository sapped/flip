import datetime as dt

import streamlit as st
import pandas as pd

from src.crud import Goal, Entry
from src.style.charts import line_chart, heatmap

from config import API_URL

PAGE_TITLE = 'Track Performance'

def write():
    st.markdown(f'# {PAGE_TITLE}')

    goals = Goal()
    entries = goals.existing_goals.sort_values(by=['has_amount'], ascending=False).loc[:,['goal','has_amount']].to_dict('index')
    # st.write(entries)
    for goal_id in entries:
        goal = entries[goal_id]['goal']
        if entries[goal_id]['has_amount'] == True:
            entries[goal_id]['tracked'] = st.checkbox(label=goal)
            if entries[goal_id]['tracked']:
                entries[goal_id]['amount'] = st.number_input(label=goal)
        else:
            entries[goal_id]['tracked'] = st.checkbox(label=goal)

    
    st.write(entries)

    

def goal_input(row):
    if row['has_amount'] == True:
        # st.write(f'AMOUNT BOY: {row.goal}')
        st.number_input(label=row.goal)
    else:
        # st.write(f'bitchass: {row.goal}')
        st.checkbox(label=row.goal)
    

if __name__=='__main__':
    write()