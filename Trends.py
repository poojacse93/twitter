import tweepy
import logging
from twitter import create_api
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def timeline(api):
    trends_result = api.trends_place(1)
    for trend in trends_result[0]["trends"]:
        print(trend["name"])

def main():
    api = create_api()
    timeline(api)

if __name__ == "__main__":
    main()