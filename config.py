import os

class TwitterConfig:
    CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
    CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')
    ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
    ACCESS_TOKEN_SECRET = os.environ.get('ACCESS_TOKEN_SECRET')

if __name__ == '__main__':
    print((os.environ.get('CONSUMER_KEY')))
    print((os.environ.get('DB_USER')))
