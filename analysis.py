import re
import math
from textblob import TextBlob

def clean(text):
        regExp = "(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"
        return ' '.join(re.sub(regExp, " ", text).split())

def sentiment(text):
        analysis = TextBlob(clean(text))
        polarity = analysis.sentiment.polarity
        result = ""
        if polarity > 0:
            result = 'positive'
        elif polarity == 0:
            result = 'neutral'
        else:
            result = 'negative'
        return [result, math.floor(polarity * 100)]

def subjectivity(text):
    return TextBlob(text).sentiment.subjectivity

def polarity(text):
    return TextBlob(text).sentiment.polarity
