import streamlit as st
from PIL import Image
import os

image = Image.open('logo.PNG')
st.set_page_config(page_title='Learn Streamlit Widgets', page_icon=image, layout='wide', initial_sidebar_state='auto')


def st_title():
    with st.expander('API Documentation - st.title(body, anchor)', expanded=False):
        st.header('st.title')
        st.write('Display text in title formatting.')
        st.image('sttitle.PNG')
