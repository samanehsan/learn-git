""" A bunch of helper functions that, when fixed up, will return the things we
need to make this website work! These functions use the weather and twitter APIs!!!
"""


###############################################
###             Problem One!                ###
###############################################

def get_city_coordinates():
    """Find the GPS coordinates for here,
    and fill in the information below
    """
    lattitude = 38.9076
    longitude = 77.0723

    return lattitude, longitude

###############################################
###             Problem Two!                ###
###############################################

def get_icon_size():
    """ Choose a number of pixels to represent the size of the weather pic.
    """
    size = 460
    return size


###############################################
###             Problem Three!              ###
###############################################

def choose_number_of_tweets():
    """ Modify this function to return the max number of tweets
    you want to appear on the site at a time!
    """
    number = 5
    return number


###############################################
###             Problem Four!              ###
###############################################

def choose_hashtag():
    """ Modify this function to return the hashtag #capwic2017
    """
    hashtag = "#capwic2017"
    return hashtag
