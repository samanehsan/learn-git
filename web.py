"""
Heroku/Python Quickstart:
https://blog.heroku.com/archives/2011/9/28/python_and_django
"""

import os
import tweepy
from flask import Flask, render_template

from helpers import choose_number_of_images, choose_number_of_tweets, choose_random_unique_items, get_api_content

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


def get_instagram_images():
    instagram_api_url = 'https://api.instagram.com/v1/tags/sparkhackathon/media/recent?client_id={}'.format(settings.CLIENT_ID)

    requested_website = get_api_content(instagram_api_url)

    data = requested_website.json()['data']
    number_of_images = choose_number_of_images()

    images = choose_random_unique_items(data, number_of_images)

    images_returned = []
    for image in images:
        image_url = image['images']['low_resolution']['url']
        images_returned.append((image['link'], image_url))

    return images_returned


def get_tweets():
    auth = tweepy.OAuthHandler(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
    auth.set_access_token(settings.ACCESS_KEY, settings.ACCESS_SECRET)
    api = tweepy.API(auth)
    tweets = tweepy.Cursor(api.search, q='#sparkhackathon')

    number_of_tweets = choose_number_of_tweets()

    tweets_html = [api.get_oembed(tweet.id)['html'] for tweet in list(tweets.items(limit=number_of_tweets))]

    return tweets_html


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
