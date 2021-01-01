import streamlit as st
st.set_page_config(initial_sidebar_state="collapsed")

import pandas as pd

# ast credit to https://github.com/MarcSkovMadsen/awesome-streamlit

import awesome_streamlit as ast
import src.pages.tracker
import src.pages.misc

# ast.core.services.other.set_logging_format()


# TBU - change app name from 'app'?

PAGES = {
    'Tracker': src.pages.tracker,
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