###############################################################################
# Project: Movie website
# #############################################################################

#################################### Media.py #################################
# Description: This file defines class Movie to allow instances of this class
# to be used in th entertaiment.py file.
###############################################################################


class Movie:
    """ The Movie class represents single movie on our website """
    def __init__(self, title, imdbData, trailer_youtube_url):
        """
        Creates an instance of Movie class with specified title,
        poster url and YouTube trailer url.

        :param title: the title of the Movie
        :param poster_image_url: poster image URL
        :param trailer_youtube_url: URL to movie trailer on YouTube
        """
        self.title = title
        self.poster_image_url = imdbData['Poster']
        self.trailer_youtube_url = trailer_youtube_url
