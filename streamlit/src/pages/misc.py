import requests
import json

import streamlit as st
import pandas as pd

from config import API_URL

PAGE_TITLE = 'Update Item'

def write():
    st.markdown(f'# {PAGE_TITLE}')

    items = read_items()
    items.set_index('id', inplace=True)
    st.write(items)

    namecol='name'
    pricecol='price'

    selected_id = st.selectbox(
        label='Choose Item to Update',
        options=list(items.index),
        format_func=lambda x: f'{x}: {items.loc[x,namecol]} (${items.loc[x,pricecol]})')

    item_original = {
        'name': items.loc[selected_id,namecol],
        'price': items.loc[selected_id,pricecol],
    }

    item_update = {}

    item_update['name'] = st.text_input(
        label='Update Item Name',
        value=item_original['name'])

    item_update['price'] = st.number_input(
        label='Update Item Price ($USD)',
        value=item_original['price']
    )

    update = st.button(label='Update')

    if update:
        updated_item = update_item(item=item_update, id=selected_id)
        if updated_item:
            st.write(updated_item)
            update = False

def update_item(item, id):
    url = f'{API_URL}/item/update/{id}'
    res = requests.post(url, json=item)
    return json.loads(res.text)

def read_items():
    url = f'{API_URL}/items/'
    res = requests.get(url)
    return pd.read_json(res.text)

if __name__=='__main__':
    write()