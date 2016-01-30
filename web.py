"""
Heroku/Python Quickstart:
https://blog.heroku.com/archives/2011/9/28/python_and_django
"""

import os
import random
import requests
import tweepy
from flask import Flask, render_template

import settings

app = Flask(__name__)


@app.route('/')
def home_page():
    instagram_pics = get_instagram_images()
    twitter_pics = get_tweets()

    return render_template(
        'home.html', name='main',
        instagram_pics=instagram_pics,
        twitter_pics=twitter_pics,
    )

'''
@app.route('/<hashtag>')
def hashtag_pages(hashtag):
    instagram_pics = get_instagram_images(hashtag)
    twitter_pics = get_tweets(hashtag)


    return render_template(
        'home.html', name='main', 
        instagram_pics=instagram_pics, 
        twitter_pics=twitter_pics,
    )
'''


def get_instagram_images(hashtag='spark'):
    instagram_api_url = 'https://api.instagram.com/v1/tags/{}/media/recent?client_id={}'.format(hashtag, settings.CLIENT_ID)

    data = requests.get(instagram_api_url).json()['data']
    number_of_images = choose_number_of_images()

    images = choose_random_unique_items(data, number_of_images)

    images_returned = []
    for image in images:
        image_url = image['images']['low_resolution']['url']
        images_returned.append((image['link'], image_url))

    return images_returned


def choose_random_unique_items(my_list, number_of_images):
    """ Given a list of items, return a random element of that list.
    Only return the item if we haven't seen it before!
    """
    if number_of_images <= len(my_list):
        return random.sample(my_list, number_of_images)
    else:
        return my_list


def choose_a_unique_item(my_list):
    return random.choice(my_list)


def get_tweets(hashtag='sparkhackathon'):
    auth = tweepy.OAuthHandler(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
    auth.set_access_token(settings.ACCESS_KEY, settings.ACCESS_SECRET)
    api = tweepy.API(auth)

    number_of_tweets = choose_number_of_tweets()


    tweets = tweepy.Cursor(api.search, q='#{}'.format(hashtag))

    tweets_html = [api.get_oembed(tweet.id)['html'] for tweet in list(tweets.items(limit=number_of_tweets))]

    return tweets_html


def choose_number_of_images():
    number = 3
    return number


def choose_number_of_tweets():
    number = 3
    return number


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
