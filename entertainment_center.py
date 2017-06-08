#Import necessary files
import fresh_tomatoes
import media


#Create instances of class Movie. These instances are the movies that are displayed on
#the website via fresh_tomatoes. Each movie contains its title, plot synopsis, image url,
#and youtube trailer url.

memento = media.Movie("Memento","A man with memory loss tries to find his wife's killer",
                      "http://www.impawards.com/2001/posters/memento_xlg.jpg",
                      "https://www.youtube.com/watch?v=0vS0E9bBSL0")

                        
pulp_fiction = media.Movie("Pulp Fiction", "The lives of multiple criminals
                           "in LA intertwine",
                           "http://www.impawards.com/1994/posters/pulp_fiction.jpg",
                           "https://www.youtube.com/watch?v=s7EdQ4FqbhY")

black_christmas= media.Movie("Black Christmas", "A deranged killer hides in a
                             "sorority house and stalks and kills its members",
                             "https://upload.wikimedia.org/wikipedia/en/thumb/9/9d/Black_christmas_poster_Canadian_authentic_theatrical.jpg/220px-Black_christmas_poster_Canadian_authentic_theatrical.jpg",
                             "https://www.youtube.com/watch?v=4gNdplqmCcQ&t=79s")

halloween = media.Movie("Halloween", "A convicted killer escapes from prison
                        "and returns to his hometown to find more victims",
                        "https://s-media-cache-ak0.pinimg.com/736x/c8/6a/76/c86a76819022e173e45815007c053217.jpg",
                        "https://www.youtube.com/watch?v=xHuOtLTQ_1I")

hot_fuzz = media.Movie("Hot Fuzz", "A big time cop from London get transferred
                       "to a small town on the British countryside",
                       "http://www.impawards.com/2007/posters/hot_fuzz_xlg.jpg",
                       "https://www.youtube.com/watch?v=ayTnvVpj9t4")

black_hawk_down = media.Movie("Black Hawk Down", "US soldiers fight for their
                              "lives in a Somalian city",
                              "http://www.impawards.com/2001/posters/black_hawk_down_ver1_xlg.jpg",
                              "https://www.youtube.com/watch?v=tnV6wM-vd9s")

#Create an array of Movies
movie = [pulp_fiction,memento,black_christmas,halloween,hot_fuzz,black_hawk_down]

#open webstie fresh_tomatoes in webbrowser 
fresh_tomatoes.open_movies_page(movie)


