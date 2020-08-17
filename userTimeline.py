import tweepy
import logging
from twitter import create_api
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def timeline(api):
    timeline = api.home_timeline()
    for tweet in timeline:
        print(f"{tweet.user.name} said {tweet.text}")

def main():
    api = create_api()
    timeline(api)

if __name__ == "__main__":
    main()
