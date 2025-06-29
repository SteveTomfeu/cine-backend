# %%
from database import SessionLocal
from models import Movie, Rating, Tag, Link

db = SessionLocal()

# %%
#Tester la récupération des films
movies = db.query(Movie).limit(10).all()
for movie in movies:
    print(f"ID : {movie.movieId}, Title : {movie.title}, Genres : {movie.genres}")
else:
    print("No movies found.")
# %%
#Récupérer les films du genre Action
actions_movies =  db.query(Movie).filter(Movie.genres.like("%Action%")).limit(10).all()
for movie in actions_movies:
    print(movie.title, movie.genres)
# %%
#Tester la récupération des évaluations
ratings = db.query(Rating).limit(10).all()
for rating in ratings:
    print(rating.rating, rating.timestamp)
# %%
high_rated_movies = (
    db.query(Movie.title, Rating.rating)
    #.join(Rating)
    .filter(Rating.rating >= 4, Movie.movieId == Rating.movieId)
    .limit(5)
    .all()
)
print(high_rated_movies)
for title, rating in high_rated_movies:
    print(title, rating)
# %%
#Récupération des tags associés aux films
tags = db.query(Tag).limit(5).all()
for tag in tags:
    print(tag.movieId, tag.userId, tag.tag)
# %%
#Tester la classe Link
links = db.query(Link).limit(5).all()
for link in links:
    print(link.movieId, link.tmdbId)
# %%
#fermer la session
db.close()
# %%
