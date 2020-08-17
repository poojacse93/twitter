import tweepy
import logging
from twitter import create_api
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def user(api):
    user = api.get_user("anandmahindra")

    print("User details:")
    print(user.name)
    print(user.description)
    print(user.location)

    print("Last 20 Followers:")
    for follower in user.followers():
        print(follower.name)

def main():
    api = create_api()
    while True:
        user(api)
        logger.info("waiting....!!!")
        time.sleep(60)

if __name__ == "__main__":
    main()