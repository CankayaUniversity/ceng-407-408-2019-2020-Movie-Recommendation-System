import pandas as pd


import pandas as pd
import numpy as np # pip install numpy==1.16.1
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import random



df = pd.read_csv(r'C:\Users\Kaan\Desktop\django_blog\blog\movie_dataset.csv')
df2 = pd.read_csv(r'C:\Users\Kaan\Desktop\django_blog\blog\MovieGenre.csv', encoding='latin-1')
data = pd.read_csv(r'C:\Users\Kaan\Desktop\django_blog\blog\main.csv', encoding='latin-1')

features = ['keywords', 'cast', 'genres', 'director']

def combine_features(row):
    return row['keywords'] + " " + row['cast'] + " " + row['genres'] + " " + row['director']

for feature in features:
    df[feature] = df[feature].fillna('')

df["combined_features"] = df.apply(combine_features, axis=1)

cv = CountVectorizer()
count_matrix = cv.fit_transform(df["combined_features"])
cosine_sim = cosine_similarity(count_matrix)

def get_title_from_index(index):
    return df[df.index == index]["title"].values[0]

def get_index_from_title(title):
     return df[df.title == title]["index"].values[0]

movie_user_likes = 'Superman'
movie_index = get_index_from_title(movie_user_likes)
similar_movies = list(enumerate(cosine_sim[movie_index]))

sorted_similar_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)[1:]

i = 0
movies = []
for element in sorted_similar_movies:
    movies.append(get_title_from_index(element[0]))
    i = i + 1
    if i > 10:
        break

# Title isimlerinden yillari cikarttik
for i in range(0, df2.shape[0]):
    index = 0
    movie_name = df2.Title.values[i]
    for j in movie_name:
        if j != '(':
            index = index + 1
        else:
            df2.Title.values[i] = movie_name[0:index - 1]





if len(data[data['title'] == movies[6]].Poster.values) == 0:
    link7 = 'https://previews.123rf.com/images/jemastock/jemastock1608/jemastock160804870/61125757-video-camera-pop-corn-movie-film-reel-cinema-icon-colorfull-illustration-vector-graphic.jpg'
else:
    link7 = data[data['title'] == movies[6]].Poster.values[0]

print(link7)
