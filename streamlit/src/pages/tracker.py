import datetime as dt

import streamlit as st
import pandas as pd

import src.crud as crud
from src.style.charts import line_chart, heatmap

from config import API_URL

PAGE_TITLE = 'Life Goals Tracker'

WEIGHT_GOALS = {
    'weekly weight loss': 1.5,
    'daily caloric target': 1800,
    'exercise surplus': 200,
}

WEEKLY_ADHERENCE_GOALS = {
    'crossfit': 3,
    'gowod': 3,
    'yoga': 1,
}

FAIL_AT_MISSING = 3

# dummy dates to play with data
fake_start_date = dt.date.today() + dt.timedelta(days=1)
fake_dates = [fake_start_date+dt.timedelta(days=i) for i in range(7)]

FAKE_DATA = {
    'crossfit': [1,0,1,0,0,1,1],
    'gowod': [0,1,0,1,1,0,0],
    'yoga': [0,0,0,0,0,1,0],
    'weight': [192.0,192.5,193.0,191.0,191.5,191.0,190.5],
    'calories': [1800,1750,1900,1800,1600,1800,1850],
    'date': fake_dates
}

def write():
    st.markdown(f'# {PAGE_TITLE}')

    # adherence = % entered as done vs. not done
    # grade scale is same as regular school for an A-, etc.
    # top of page, show cumulative adherence to all goals
    # breakdown adherence to goals

    expander1 = st.beta_expander('Track', expanded=True)
    expander2 = st.beta_expander('Review', expanded=True)

    with expander1:
        track()
        
    with expander2:
        review()

    # adherence
    # show % adherence

    # 2 cols
    # col 1 - adherence
        # show % adherence
        # show grade

    # col 2 - all time
        # show % ad

# view tracker entries, trailing seven days adherence
# can change 7 days to MTD, YTD, 
# min of selected period or days that have lapsed sinced kickoff
def review():
    df = pd.DataFrame(FAKE_DATA)
    df = df[['date','weight','calories','crossfit','gowod','yoga']]
    df.set_index('date',inplace=True)
    df = df.sort_values(by=['date'], ascending=False)
    st.write(df)

    st.markdown('### Weight')
    line_chart(df['weight'])
    st.markdown('### Calories')
    line_chart(df['calories'])
    st.markdown('### Tracking')
    st.write(heatmap(df[['crossfit','gowod','yoga']]))

# must track all days
# load cards with dates without tracker between latest tracked and today
# you lose at three untracked days (three strikes, you're out) and have to restart
# you have to click a button that says a custom message
def track():
    st.selectbox(label='Dates to track', options=['Date1','Date2'])

    # TBU modify which goals you wish to track in this way
    # TBU stream of time, you can remove certain goals from the stack
    # TBU add more to the stack. It's a daily stream
    trackers = {
        'weight': st.number_input(label='Weight'),
        'calories': st.number_input(label='Calories'),
        'crossfit': st.checkbox(label='Crossfit'),
        'gowod': st.checkbox(label='GOWOD'),
        'yoga': st.checkbox(label='Yoga'),
    }

    create = st.button(label='Create')

    if create:
        tracker = Tracker.submit_tracker(tracker)
        if item:
            st.write(item)
            create = False

if __name__=='__main__':
    write()