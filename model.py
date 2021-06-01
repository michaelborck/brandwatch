import re
import urllib
import pandas as pd
import analysis as sa

from collections import Counter
from interface import search, connect


def as_df(query):
    # Initialize empty dataframe
    df = pd.DataFrame({
        'tweet': [],
        'clean_tweet': [],
        'predicted-sentiment': [],
        'polarity':[],
        'subjectivity':[],
        'date': [],
        'likes': [],
        'retweets': [],
        'followers': [],
        'verified_user':[],
        'location' : []
    })
    tweets = search(connect(), query, limit = 200)
    # Add data for each tweet
    for tweet in tweets:
        # Skip iteration if tweet is empty
        if tweet.full_text in ('', ' '):
            continue
        # Make predictions
        sentence = sa.clean(tweet.full_text)
        sentiment, polarity = sa.sentiment(sentence)
        subjectivity =  sa.subjectivity(sentence)

        # Append new data
        df = df.append({
            # 'tweet': tweet.text,
            'tweet': tweet.full_text,
            'clean_tweet': sentence,
            'predicted-sentiment': sentiment,
            'polarity': polarity,
            'subjectivity': subjectivity,
            'date': tweet.created_at,
            'likes': tweet.favorite_count,
            'retweets': tweet.retweet_count,
            'followers': tweet.user.followers_count,
            'verified_user': tweet.user.verified,
            'location': tweet.user.location }, ignore_index=True)
    # Remove time, only care about day
    df['date'] = pd.to_datetime(df['date']).dt.date
    return df


def as_hashtags(tweets):
    # get all hashtags
    hashtags = re.findall(r"#\w+",  tweets)
    hashtags = Counter(hashtags).most_common()[:6]
    return hashtags

def as_urls(tweets):
    for tweet in tweets:
        urls = re.findall("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", tweets)
        for url in urls:
            try:
                opener = urllib.request.build_opener()
                request = urllib.request.Request(url)
                response = opener.open(request)
                actual_url = response.geturl()
                print(actual_url)
            except:
                print(url)
    return urls
