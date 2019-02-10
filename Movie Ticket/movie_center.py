import fresh_tomatoes
import media
toy_story=media.Movie("toy_story",
                      "toys are happy",
                      "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
                      "https://www.google.co.in/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=2ahUKEwjDoujjgZ7gAhWKtY8KHQ3bAEQQ3ywwAHoECAcQAw&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DKYz2wyBy3kc&usg=AOvVaw0z39p4CAtfAw4uZDhaE4vX")
#print(toy_story.storyline)
#toy_story.show_trailer()
movies=[toy_story]
#fresh_tomatoes.open_movies_page(movies)
print(media.Movie.VALID_RATINGS)
