""" A bunch of helper functions that, when fixed up, will return the things we
need to make this website work!
"""

## Import python libraries we need up here.

import requests

###############################################
###             Problem One!                ###
###############################################

def choose_random_unique_items(my_list, number_of_images):
    """ Given a list of items, return a *random* element of that list.
    Only return the item if we haven't seen it before! Get a sample. A random sample.
    """
    if number_of_images <= len(my_list):
        # This is the case if our hashtag has enough images to meet our number request
        # figure out the one line that we can return that will give us a random member of the
        # list, with no repeats.
        return ?????
    else:
        ## If we ask for more images that we have, then just return everything there is
        return my_list


###############################################
###             Problem Two!                ###
###############################################

def choose_number_of_images():
    """ Modify this function to return a number of instagram photos
    you want to appear on the site at a time! Because of how the instagram API works,
    it won't return more than 20 photos at once.
    """
    number = ??
    return number


###############################################
###             Problem Three!              ###
###############################################

def choose_number_of_tweets():
    """ Modify this function to return a number of tweets
    you want to appear on the site at a time!
    """
    number = ??
    return number


###############################################
###             Problem Four!              ###
###############################################

def get_api_content(api_url):
    """ Modify this function to use a commmon python library to go to an api_url (get it!) and give you
    back what it finds. Request the site, and get its contents. Hint Hint.
    """
	return requests.get(api_url)

