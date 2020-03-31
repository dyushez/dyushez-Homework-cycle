import pandas as pd

movies = pd.read_csv('movies.csv', index_col='movieId')
tags = pd.read_csv('tags.csv', index_col='movieId')

# merge movies and tags data frames in on movieId
data_tags_movies = pd.merge(tags, movies, on='movieId')

print(data_tags_movies)
