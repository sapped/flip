# stdlib imports
import time

# library imports
import streamlit as st

# local imports
from config import API_URL

PAGE_TITLE = 'Miscellaneous Gags'

def write():
    st.markdown(f'# {PAGE_TITLE}')

    st.markdown('### Seconds since January 1, 1970')
    st.write('Press r to refresh the page')
    st.write(time.time())

if __name__=='__main__':
    write()