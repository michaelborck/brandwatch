import tweepy
from config import TwitterConfig as twc

def connect():
    auth = tweepy.OAuthHandler(twc.CONSUMER_KEY, twc.CONSUMER_SECRET)
    auth.set_access_token(twc.ACCESS_TOKEN, twc.ACCESS_TOKEN_SECRET)
    return tweepy.API(auth)

def search(api, query, limit = 1000, language = "en", mode = 'extended'):
    searched_tweets = []
    last_id = -1
    while len(searched_tweets) < limit:
        count = limit - len(searched_tweets)
        try:
            new_tweets = api.search(q=query, count=count,
                        max_id=str(last_id - 1),language="en", tweet_mode=mode)
            if not new_tweets:
                break
            searched_tweets.extend(new_tweets)
            last_id = new_tweets[-1].id
        except tweepy.TweepError as e:
            # depending on TweepError.code, one may want to retry or wait
            # to keep things simple, we will give up on an error
            print("Error : " + str(e))
            break
    return searched_tweets
