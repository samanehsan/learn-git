""" Heroku/Python Quickstart: https://blog.heroku.com/archives/2011/9/28/python_and_django"""

import os
import random
import requests
from flask import Flask

import tweepy

import settings


app = Flask(__name__)


@app.route('/')
def home_page():
    return 'Hello from the SPARK learn-a-thon!'


def get_instagram_image():
    instagram_api_url = 'https://api.instagram.com/v1/tags/spark/media/recent?client_id={}'.format(settings.CLIENT_ID)

    data = requests.get(instagram_api_url).json()['data']
    number_of_images = choose_number_of_images()

    images_returned = []
    for image in number_of_images:
        images_returned.append(random.choice(data)['images']['low_resolution']['url'])

    return images_returned


def get_tweets():
    auth = tweepy.OAuthHandler(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
    auth.set_access_token(settings.ACCESS_KEY, settings.ACCESS_SECRET)
    api = tweepy.API(auth)

    number_of_tweets = choose_number_of_tweets()

    tweets = tweepy.Cursor(api.search, q='#spark')
    return tweets.items(limit=number_of_tweets)


def choose_number_of_images():
    number = 3
    return number


def choose_number_of_tweets():
    number = 3
    return number


if __name__ == '__main__':
    # port = int(os.environ.get("PORT", 5000))
    # app.run(host='0.0.0.0', port=port)

