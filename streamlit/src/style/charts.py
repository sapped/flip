import plotly.express as px
import pandas as pd

def line_chart(df):
    fig = px.line(df, x='date', y='weight', title='Weight')
    fig.show()

def heatmap(df):
    df.style.apply(lambda x: ['background: green' if x > 1 else ''])
    return df