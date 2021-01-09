# stdlib imports

# library imports
import streamlit as st
import pandas as pd
import awesome_streamlit as ast # https://github.com/MarcSkovMadsen/awesome-streamlit

# local imports
import src.pages.goals
import src.pages.entries
import src.pages.misc
from users.users import get_user

st.set_page_config(
    initial_sidebar_state="collapsed",
    page_title='flip.RIP')

# TBU - change app name from 'app'?

PAGES = {
    'Track Performance': src.pages.entries,
    'Manage Goals': src.pages.goals,
    'Miscellaneous Gags': src.pages.misc,
}

def main():
    user = get_user()
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))
    st.sidebar.markdown(f'Logged in as **{user}**.')
    
    page = PAGES[selection]

    with st.spinner(f"Loading {selection} ..."):
        ast.shared.components.write_page(page)

if __name__=='__main__':
    main()