from database import SessionLocal
from query_helpers import *

db = SessionLocal()

# movie =get_movies(db, limit=10)
# for film in movie:
#     print(film.movieId, film.title, film.genres)

rating = get_rating(db, movie_id=1, user_id=1)
print(rating.userId, rating.movieId, rating.rating)
db.close()