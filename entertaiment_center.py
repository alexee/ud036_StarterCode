from media import Movie

import fresh_tomatoes
import requests

# OMDB api key
api_key = "1c23f626";

# request data from OMDB IMDB API
def requestImdbData(imdbId):
    request_uri = "http://www.omdbapi.com/?i=" + imdbId + "&apikey=" + api_key;
    response = requests.get(request_uri).json();
    return response

# First create 4 instances for each of movies that we want to display on our website
movie_terminator = Movie("The Terminator", requestImdbData("tt0088247"),
    "https://www.youtube.com/watch?v=QIcomuI1j7I")

movie_superbad = Movie("Superbad", requestImdbData("tt0829482"),
    "https://www.youtube.com/watch?v=q3UFV1in5Qk")

movie_red_sparrow = Movie("Red Sparrow", requestImdbData("tt2873282"),
    "https://www.youtube.com/watch?v=PmUL6wMpMWw")

movie_bean = Movie("Bean", requestImdbData("tt0118689"),
    "https://www.youtube.com/watch?v=OxLQZVmKWEo")

# Put all movies into a list
all_movies = [movie_terminator, movie_superbad, movie_red_sparrow, movie_bean]

# now generate HTML page and open it in the webbrowser
fresh_tomatoes.open_movies_page(all_movies)
