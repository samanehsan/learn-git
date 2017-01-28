"""
Heroku/Python Quickstart:
https://blog.heroku.com/archives/2011/9/28/python_and_django
"""

import os
import tweepy
import requests
from flask import Flask, render_template

from helpers import(
    choose_number_of_tweets,
    get_city_coordinates,
    get_icon_size,
    choose_hashtag
)

import settings

app = Flask(__name__)


@app.route('/')
def home_page():
    weather_data = get_weather()
    twitter_pics = get_tweets()

    return render_template(
        'home.html', name='main',
        weather_data=weather_data,
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


def get_weather():

    lattitude, longitude = get_city_coordinates()
    icon_size = get_icon_size()

    weather_url = 'http://api.openweathermap.org/data/2.5/weather?units=imperial&lat={}&lon={}&APPID={}'.format(
        lattitude,
        longitude,
        settings.WEATHER_API_KEY
    )
    weather_api_data = requests.get(weather_url).json()

    return {
        'city': weather_api_data['name'],
        'temp': weather_api_data['main']['temp'],
        'description': weather_api_data['weather'][0]['description'],
        'icon': 'http://openweathermap.org/img/w/{}.png'.format(weather_api_data['weather'][0]['icon']),
        'icon_size': icon_size
    }


def get_tweets():
    auth = tweepy.OAuthHandler(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
    auth.set_access_token(settings.ACCESS_KEY, settings.ACCESS_SECRET)
    api = tweepy.API(auth)
    tweets = tweepy.Cursor(api.search, q=choose_hashtag())

    number_of_tweets = choose_number_of_tweets()

    tweets_html = [api.get_oembed(tweet.id)['html'] for tweet in list(tweets.items(limit=number_of_tweets))]

    return tweets_html


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
