import tweepy
import logging
from twitter import create_api
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def create(api):
    api.update_status("Truth can only be found in one place: the code!! ~Robert C.Martin")

def main():
    api = create_api()
    
    create(api)

if __name__ == "__main__":
    main()