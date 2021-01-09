# library imports
import plotly.express as px
import pandas as pd
import streamlit as st

def table_cols(df_in):
    df = df_in.reset_index()
    st.table(df)
    return 0

    # TBU - row-wise containers necessary to implement this
    rows, cols = df.shape[0], df.shape[1]
    col_headers = st.beta_columns(cols)
    col_placeholders = st.beta_columns(cols)
    
    for colnum, col in enumerate(df.columns):
        with col_headers[colnum]:
            st.write(col)
    
    st.markdown('***')
    
    for colnum, col in enumerate(df.columns):
        with col_placeholders[colnum]:    
            for row in df[col]:
                st.write(row)

    




    return 0

def line_chart(df):
    fig = px.line(df, x='date', y='weight', title='Weight')
    fig.show()

def heatmap(df):
    df.style.apply(lambda x: ['background: green' if x > 1 else ''])
    return df
