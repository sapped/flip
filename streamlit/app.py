# stdlib imports

# library imports
import streamlit as st
import pandas as pd
import awesome_streamlit as ast # https://github.com/MarcSkovMadsen/awesome-streamlit

# local imports
import src.pages.new_tracker
import src.pages.goals
import src.pages.entries
import src.pages.misc
from user.user import User

st.set_page_config(
    initial_sidebar_state="collapsed",
    page_title='Flip that rip')

PAGES = {
    'Goal Tracker v2': src.pages.new_tracker,
    'Track Performance': src.pages.entries,
    'Manage Goals': src.pages.goals,
    'Miscellaneous Gags': src.pages.misc,
}

def main():
    user = User()
    st.write(user)
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))
    st.sidebar.markdown(f'Logged in as **{user.current_username}**.')
    
    page = PAGES[selection]

    with st.spinner(f"Loading {selection} ..."):
        ast.shared.components.write_page(page)

if __name__=='__main__':
    main()