import streamlit as st

class TwitterConfig:
    CONSUMER_KEY = st.secrets['CONSUMER_KEY']
    CONSUMER_SECRET = st.secrets['CONSUMER_SECRET']
    ACCESS_TOKEN = st.secrets['ACCESS_TOKEN']
    ACCESS_TOKEN_SECRET = st.secrets['ACCESS_TOKEN_SECRET']
