""" A bunch of helper functions that, when fixed up, will return the things we
need to make this website work!
"""

## Import python libraries we need up here.


import requests

import random

###############################################
###             Problem One!                ###
###############################################

def get_city_coordinates():
    """Find the GPS coordinates for Charlottesville,
    and fill in the information below
    """
    lattitude = 38.0293
    longitude = -78.4767

    return lattitude, longitude

###############################################
###             Problem Two!                ###
###############################################

def get_icon_size():
    """ Modify this function to return a number of instagram photos
    you want to appear on the site at a time! Because of how the instagram API works,
    it won't return more than 20 photos at once.
    """
    size = 100
    return size


###############################################
###             Problem Three!              ###
###############################################

def choose_number_of_tweets():
    """ Modify this function to return a number of tweets
    you want to appear on the site at a time!
    """
    number = 10
    return number


###############################################
###             Problem Four!              ###
###############################################

def get_api_content(api_url):
    """ Modify this function to use a commmon python library to go to an api_url (get it!) and give you
    back what it finds. Request the site, and get its contents. Hint Hint.
    """
    return requests.get(api_url)
