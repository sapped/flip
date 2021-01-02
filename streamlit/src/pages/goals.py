# libraries
import streamlit as st
import pandas as pd

# local
from src.crud import Goal
from src.style.charts import line_chart, heatmap
from config import API_URL


PAGE_TITLE = 'Manage Goals'

def write():
    st.markdown(f'# {PAGE_TITLE}')

    # initiate & read goals
    goals = Goal()
    st.markdown('### List Existing Goals')
    st.write(goals.existing_goals)
    
    # create goal
    create_goal(goals)
    
    # delete goal
    delete_goal(goals)

def create_goal(goals):
    st.markdown('### Create New Goal')
    new_goal = {
        'goal': st.text_input(label='Goal Name'),
        'has_amount': st.checkbox(label='Goal tracks an amount? (weight, calories, etc.)'),
    }

    create = st.button(label='Create goal')

    if create:
        goal_response = goals.create_goal(new_goal)
        if goal_response is not None:
            create = False
        st.write(goal_response)

def delete_goal(goals):
    st.markdown('### Delete Existing Goal')
    delete_id = st.selectbox(
        label='Choose goal to delete',
        options=goals.existing_goals.index,
        format_func=lambda x: goals.existing_goals.loc[x,'goal'])
    
    delete = st.button(label='Delete goal')
    
    if delete:
        goal_response = goals.delete_goal(delete_id)
        if goal_response is not None:
            delete = False
        st.write(goal_response)

if __name__=='__main__':
    write()