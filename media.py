import webbrowser


class Movie():
    """ Movie() creates a new object through which instances of
    the type Movie can be made """
    def __init__(self, movie_title, poster_image, trailer_youtube):
        """ The constructor method is called when a new object is instantiated
         and the variables below are assigned """
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
