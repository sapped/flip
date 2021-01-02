import datetime as dt

import streamlit as st
import pandas as pd

import src.crud as crud
from src.style.charts import line_chart, heatmap

from config import API_URL

PAGE_TITLE = 'Life Goals Tracker'

def write():
    st.markdown(f'# {PAGE_TITLE}')

    return
    expander1 = st.beta_expander('Track', expanded=True)
    expander2 = st.beta_expander('Review', expanded=True)

    # goals n shit

if __name__=='__main__':
    write()