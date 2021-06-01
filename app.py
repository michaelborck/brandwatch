#!/usr/bin/env python
# -*- coding: utf-8 -*-

import model
import plots
import dateutil
import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px

def main():
    st.set_page_config(layout="wide", page_title='Brandwatch')
    st.title("Brandwatch")
    st.subheader('Search Twitter')

    st.sidebar.header("About App")
    st.sidebar.info("A Twitter Sentiment analysis project which will scrap \
        twitter for the topic selected by the user. The extracted \
        tweets will then be used to determine the Sentiments of those \
        tweets. The different Visualizations will help us get a feel of the \
        overall mood of the people on Twitter regarding the topic we select.")
    st.sidebar.info("This app uses the standard twitter API. The standard API\
         only allows you to retrieve tweets up to 7 days ago and is limited to\
         scraping 18,000 tweets per a 15 minute window.")

    # Get user input
    query = st.text_input('', '#')


    # As long as the query is valid (not empty or equal to '#')...
    if query != '' and query != '#':
        with st.spinner(f'Searching for and analysing {query}...'):
            df = model.as_df(query)

            col1, col2 = st.beta_columns(2)
            with col1:
                fig = plots.sentiment_over_time(df)
                st.plotly_chart(fig)

                text = " ".join(tweet for tweet in df.clean_tweet)
                st.image(plots.tweet_cloud(text))

            with col2:
                # daily volume
                fig = plots.tweets_per_day(df)
                st.plotly_chart(fig)

                fig = plots.sentiment_proportions(df)
                st.plotly_chart(fig)

if __name__ == "__main__":
    # calling main function
    main()
