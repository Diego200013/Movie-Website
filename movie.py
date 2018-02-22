import webbrowser
class Movie():


 """this class allows us to store information about the movie, which takes it by parameters"""

 def __init__(self,movie_title,movie_storyline,poster_image, trailer_youtube,director_movie,launch_date):
		self.title=movie_title
		self.storyline=movie_storyline
		self.poster_image_url=poster_image
		self.trailer_youtube_url=trailer_youtube
		self.director=director_movie
		self.launch=launch_date

 """this function allows you to open the trailer of a movie on youtube, with the assigned url"""

	#def show_trailer(self):
		#webbrowser.open(self.trailer_youtube_url)
