import streamlit as st
st.set_page_config(
    initial_sidebar_state="collapsed",
    page_title='flip.RIP')

import pandas as pd

# ast credit to https://github.com/MarcSkovMadsen/awesome-streamlit

import awesome_streamlit as ast
import src.pages.goals
import src.pages.entries
import src.pages.misc

# TBU - change app name from 'app'?

PAGES = {
    'Track Performance': src.pages.entries,
    'Manage Goals': src.pages.goals,
    'Misc': src.pages.misc,
}

def main():
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))
    
    page = PAGES[selection]

    with st.spinner(f"Loading {selection} ..."):
        ast.shared.components.write_page(page)

if __name__=='__main__':
    main()