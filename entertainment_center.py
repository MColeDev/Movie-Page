import media
import fresh_tomatoes

""" Data for each movie is entered so it can be passed
    to the corresponding webpage """

toy_story = media.Movie(
    "Toy Story",
    "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie(
    "Avatar",
    "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https://youtu.be/5PSNL1qE6VY")

alien = media.Movie(
    "Alien",
    "http://upload.wikimedia.org/wikipedia/en/c/c3/Alien_movie_poster.jpg",
    "https://youtu.be/LjLamj-b0I8")

titan_ae = media.Movie(
    "Titan AE",
    "https://upload.wikimedia.org/wikipedia/en/7/75/Titan_AE_One_Sheet.jpg",
    "https://youtu.be/8E_t8D-18Qo")

cloud_atlas = media.Movie(
    "Cloud Atlas",
    "https://upload.wikimedia.org/wikipedia/en/2/20/Cloud_Atlas_Poster.jpg",
    "https://youtu.be/ByehYal_cCs")

highlander = media.Movie(
    "Highlander",
    "https://upload.wikimedia.org/wikipedia/en/0/0b/Highlander_1_poster.jpg",
    "https://youtu.be/omOZyLmNMJs")

movies = [toy_story, avatar, highlander, alien, titan_ae, cloud_atlas]

""" This generates an HTML file which accepts the information
    from the movies list """
fresh_tomatoes.open_movies_page(movies)
