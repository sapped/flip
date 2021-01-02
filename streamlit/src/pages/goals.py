import datetime as dt

import streamlit as st
import pandas as pd

from src.crud import Goal
from src.style.charts import line_chart, heatmap

from config import API_URL

PAGE_TITLE = 'Manage Goals'

def write():
    st.markdown(f'# {PAGE_TITLE}')

    existing_goals = read_goals()
    st.write(existing_goals)
    create_goal()
    delete_goal(existing_goals)

def read_goals():
    st.markdown('### List Existing Goals')
    return Goal.read_goals()

def create_goal():
    st.markdown('### Create New Goal')
    new_goal = {
        'goal': st.text_input(label='Goal Name'),
        'has_amount': st.checkbox(label='Goal tracks an amount? (weight, calories, etc.)'),
    }

    create = st.button(label='Create goal')

    if create:
        goal = Goal.create_goal(new_goal)
        if goal is not None:
            create = False
        st.write(goal)

def delete_goal(df):
    st.markdown('### Delete Existing Goal')
    delete_id = st.selectbox(
        label='Choose goal to delete',
        options=df.index,
        format_func=lambda x: df.loc[x,'goal'])
    
    delete = st.button(label='Delete goal')
    
    if delete:
        goal = Goal.delete_goal(delete_id)
        if goal is not None:
            delete = False
        st.write(goal)

if __name__=='__main__':
    write()