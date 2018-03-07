from media import Movie

import fresh_tomatoes

# First create 4 instances for each of movies that we want to display on our website

movie_terminator = Movie("The Terminator", "terminator1.jpg",
    "https://www.youtube.com/watch?v=QIcomuI1j7I")

movie_superbad = Movie("Superbad", "superbad1.jpg",
    "https://www.youtube.com/watch?v=q3UFV1in5Qk")

movie_red_sparrow = Movie("Red Sparrow", "redsparrow.jpg",
    "https://www.youtube.com/watch?v=PmUL6wMpMWw")

movie_bean = Movie("Bean", "bean.jpg",
    "https://www.youtube.com/watch?v=OxLQZVmKWEo")

# Put all movies into a list
all_movies = [movie_terminator, movie_superbad, movie_red_sparrow, movie_bean]

# now generate HTML page and open it in the webbrowser
fresh_tomatoes.open_movies_page(all_movies)
