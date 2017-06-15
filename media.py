# Import necessary files
import webbrowser


class Movie():
    """This class stores movie information for use in fresh_tomatoes.py"""

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title  # stores movie title
        self.storyline = movie_storyline  # stores movie storyline
        self.poster_image_url = poster_image  # stores poster image url
        self.trailer_youtube_url = trailer_youtube  # stores youtube trailer url # noqa

    def show_trailer(self):
        # Used to open movie's youtube trailer
        webbrowser.open(self.trailer_youtube_url)
