import movie
import fresh_tomatoes


"""here are the sipnosis of the films keep in variables because i want that the code view ordered"""

                
toy = "Sheriff Woody and Star Command Buzz Lightyear, along with the rest of their inseparable roommates,\
 were handed over by an Andy about to enter the university to a little girl named Bonnie, who received this excited gift\
But now the toys are back in charge. What new adventures await you in this fourth installment? "

avatar="A moon of the planet Polyphemus inhabited by a humanoid race called na 'vi\
with which humans are in conflict because one of their clans is seated around a gigantic tree that covers an immense\
vein of a highly valued mineral and that would be the solution to the energy problems of the Earth: the unobtainium "

titanic="It relates the relationship of Jack Dawson and Rose DeWitt Bukater, two young people who know each other and \
 fall in love aboard the ocean liner RMS Titanic on its maiden voyage from Southampton, England, to New York, USA. UU.,\
In April 1912,Belonging to different social classes",

red_dog="True Blue explores the famous Australian legend of a dog that supposedly wandered all over Australia during the 70s.\
After his father dies and his mother is sent to a mental hospital, a child goes to live in the hospital. farm of his grandfather \
 After a storm the boy finds a puppy covered in blue paint and convinces his grandfather so that this canine stays with him."

jurassi="After the disappearance of the Jurassic World theme park on Nublar Island, dinosaurs roam freely around the island \
 for four years until a volcanic eruption threatens their existence. Claire Dearing, former park administrator, now founded the\
 Dinosaur Protection Group, an organization dedicated to saving dinosaurs,Claire recruits Owen Grady."

wonder= "Uggie Pullman (Jacob Tremblay) is a child born with a facial malformation. Now, after ten years of hospital in hospital\
 and long periods in your home, you will have to face a great challenge: to attend school for the first time. Thanks to the support \
 of his parents, Isabel (Julia Roberts) and Nate (Owen Wilson), Auggie tried to fit together new classmates and teachers."

winter_river="It is winter in the Wind River Indian Reservation in Wyoming (USA) When Cory Lambert, Fish and Wildlife Service agent,\
 discovers the frozen body of Natalie Hanson, 18, without shoes and winter clothes and with the hose blood  Newbie FBI special\
 agent Jane Banner arrives to determine if a murder has been committed. The next day, Jane discovers by Natalie's \
father that her daughter was dating a new boyfriend, but does not know the man's name or whereabouts"

deadpol="Wade Wilson begins to tell a taxi driver his story about how he is about to take revenge on the evil Francis,\
the man who ruined his face and wants him to return to normal in order to return to the woman he loves. In the same way\
 that he tries to pay the free ride to the taxi driver, Wade gives some loving advice to the taxi driver, which includes\
  kidnapping his girlfriend's other suitor and then killing the guy. While I waited on the railings of a bridge for Francis's men to pass"

blade_run="Thirty years have passed since the events that occurred in Blade Runner (1982). Agent K (Ryan Gosling), a 'blade runner' fighter-Replicators \
of the Los Angeles Police Department, discovers a secret that has been buried for a long time and that has the potential to carry society into chaos.  research led him to the search for the legendary Rick Deckard (Harrison Ford), a former blade runner unknown whereabouts, who has been missing for 30 years."


#example
#movie=movie.Movie("",
                  #  "",
                   # "",
                    # "",
                     #"",
                     #"")
     
#information of the films

toy_story= movie.Movie("toy story",
	                    toy,
	                    "http://es.web.img3.acsta.net/pictures/14/11/07/15/51/086299.jpg",
	                    "https://www.youtube.com/watch?v=Bj4gS1JQzjk",
	                    "Director: Josh Cooley",
	                    "Launch Date: June,20th 2019")



avatar= movie.Movie("avatar",
	                avatar,
	                "https://vignette1.wikia.nocookie.net/james-camerons-avatar/images/a/a7/Caratula_de_Avatar.png/revision/latest?cb=20150218032222&path-prefix=es",
	                "https://www.youtube.com/watch?v=UrdfmlhYRfs",
	                "Director: James Cameron",
	                "Launch Date: December,19th 2009")



titanic=movie.Movie("Titanic",
                    titanic,
                    "https://pics.filmaffinity.com/titanic-321994924-large.jpg",
                    "https://www.youtube.com/watch?v=zCy5WQ9S4c0",
                    "Director:  James Cameron",
                    "Launch Date: February,13rd 1998")



red_dog=movie.Movie("red dog: true blue",
	               red_dog,
	               "https://www.booktopia.com.au/http_coversbooktopiacomau/big/9781742752259/red-dog.jpg",
	                "https://www.youtube.com/watch?v=ys9njXUXCIk",
	                "Director:Kriv Stenders",
                    "Launch Date: December,26th 2016")

jurassic=movie.Movie("Jurassic World",
	                 jurassi,
	                "http://i.imgur.com/4hvGoxS.jpg",
	                "https://www.youtube.com/watch?v=vn9mMeWcgoM",
	                "Director:Juan Antonio Bayona",
                    "Launch Date: June,22nd 2018")

wonder=movie.Movie("Wonder",
                    wonder, 
                    "https://images-na.ssl-images-amazon.com/images/M/MV5BNTA2MTU1NTkxOV5BMl5BanBnXkFtZTgwNjk4MjE0MjI@._V1_SY1000_CR0,0,648,1000_AL_.jpg",
                    "https://www.youtube.com/watch?v=AWgLSlxOAt4",
                    "Director: Stephen Chbosky",
                    "Launch Date: November,16th 2017")

winter=movie.Movie("wind river",
                    winter_river, 
                    "https://i.ytimg.com/vi/1MXHP4UaYHY/movieposter.jpg",
                    "https://www.youtube.com/watch?v=s7WuKdVhrmA",
                    "Director: Taylor Sheridan",
                    "Launch Date: August,4th 2017")

deadpool=movie.Movie("Deadpool",
	                 deadpol,
                    "https://pics.filmaffinity.com/deadpool-834516798-large.jpg",
                    "https://www.youtube.com/watch?v=0JnRdfiUMa8",
                    "Director Tim Miller",
                    "Launch Date: February,11th 2016")

blade=movie.Movie("blade runner 2049",
                     blade_run, 
                    "http://es.web.img3.acsta.net/pictures/17/08/25/11/58/463146.jpg",
                    "https://www.youtube.com/watch?v=gCcx85zbxz4",
                    "Director Ridley Scott",
                    "Launch Date: March,16th 1983")



#add films to list
movies=[toy_story,avatar,titanic,red_dog,jurassic,wonder,winter,deadpool,blade]

#open movies in the web
fresh_tomatoes.open_movies_page(movies)
