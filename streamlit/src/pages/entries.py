# stlib imports
import time, pytz
import datetime as dt

# library imports
import streamlit as st
import pandas as pd
import numpy as np

# local imports
from src.crud import Goal, Entry
from src.style.charts import line_chart, heatmap, table_cols
from config import API_URL
from src.style.stringformats import es_date_format

PAGE_TITLE = 'Track Performance'

def write():
    st.markdown(f'# {PAGE_TITLE}')

    # initialize crud objects
    goals = Goal()
    if goals.existing_goals.empty == True:
        footer()
        return

    entries = Entry()
    # main app
    if entries.existing_entries.empty == True:
        st.markdown('### Create your first entry!')
        st.write('This page will change after refresh (press r)')
        create_entry(entries, goals)
        return

    st.markdown('### Review Existing Entries')
    # first get entry_pivot & don't modify its data
    entry_pivot = read_entries(entries,goals)
    
    # then, format it as out_existing_entries
    show_existing_entries(entry_pivot)
    col1, col2 = st.beta_columns(2)
    with col1:
        st.markdown('### Create New Entry')
        create_entry(entries, goals)
    with col2:
        st.markdown('### Delete an Existing Entry')
        delete_entry(entries, entry_pivot)
    
    footer()
    
def footer():
        st.write('Feel free to delete or create new goals! \
        Click on the little arrow in the top left \
        to open navigation, then \
        select the appropriate page.')


# FORMAT presentation of existing entries
def show_existing_entries(df_in):
    df = df_in.copy()
    df.reset_index(inplace=True)
    df['date'] = df['date'].apply(es_date_format)
    df.set_index('date', inplace=True)
    
    with st.beta_expander(label='Goal-wise review', expanded=True):
        table_cols(df)

    with st.beta_expander(label='Date-wise review', expanded=False):
        datewise = df.copy()

        date = st.selectbox(label='Choose date to review',
        options=datewise.index)
        datewise = datewise.loc[datewise.index==date]
        table_cols(datewise.T)
    
    return 0

# DELETE entry
def delete_entry(entries, df):
    # time formats: https://www.tutorialspoint.com/python/time_strftime.htm
    # time zone annoyances: https://stackoverflow.com/questions/22800079/converting-time-zone-pandas-dataframe
    # choose timestamp of entry to remove 
    id = st.selectbox(
        label='Choose entry to delete',
        options=df.index,
        format_func=lambda x: es_date_format(x))
    # get list of indices of matches
    delete_id_list = entries.existing_entries.loc[entries.existing_entries['date']==id].index.tolist()

    # delete the entry (speak to API)
    delete = st.button(label='Delete entry')
    if delete:
        delete_response = entries.delete_entry(delete_id_list)
        if delete_response is not None:
            delete = False

# READ entries
def read_entries(entries, goals):
    df = entries.existing_entries
    df['goal'] = df['goal_id'].map(goals.existing_goals['goal'])
    df['has_amount'] = df['goal_id'].map(goals.existing_goals['has_amount'])
    df['entry'] = np.where(df['has_amount']==True, df['amount'], df['tracked'])
    df = pd.pivot_table(df,columns=['goal'],index=['date'],values=['entry'],dropna=False)
    # drop multi-index col level: https://stackoverflow.com/questions/22233488/pandas-drop-a-level-from-a-multi-level-column-index
    df.columns = df.columns.droplevel(0)
    return df

# CREATE entry
def create_entry(entries, goals):
    st.write('Select what you have tracked today. When checked, certain items may ask for more detail.')
    
    now = time.time()

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