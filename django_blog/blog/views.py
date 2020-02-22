from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.http import JsonResponse
from .models import Blog
import pandas as pd
import numpy as np # pip install numpy==1.16.1
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import random
df = pd.read_csv(r'C:\Users\Kaan\Desktop\django_blog\blog\movie_dataset.csv')




def post_list(request):

    df = pd.read_csv(r'C:\Users\Kaan\Desktop\django_blog\blog\movie_dataset.csv')
    data = pd.read_csv(r'C:\Users\Kaan\Desktop\django_blog\blog\main.csv', encoding='latin1')
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

    # movie_user_likes = request.POST['movie_name']
    number = random.randrange(0, 4500)
    movie_user_likes = str(df["title"][number])
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



    if len(data[data.Title == movies[0]].Poster.values) == 0:
        link1 = 'https://as2.ftcdn.net/jpg/01/23/50/75/500_F_123507588_WM22wAfkxrFwuNzHvxejP3AxnQTGCvIY.jpg'
    else:
        link1 = data[data.Title == movies[0]].Poster.values[0]

    if len(data[data.Title == movies[1]].Poster.values) == 0:
        link2 = 'https://as2.ftcdn.net/jpg/01/23/50/75/500_F_123507588_WM22wAfkxrFwuNzHvxejP3AxnQTGCvIY.jpg'
    else:
        link2 = data[data.Title == movies[1]].Poster.values[0]

    if len(data[data.Title == movies[2]].Poster.values) == 0:
        link3 = 'https://as2.ftcdn.net/jpg/01/23/50/75/500_F_123507588_WM22wAfkxrFwuNzHvxejP3AxnQTGCvIY.jpg'
    else:
        link3 = data[data.Title == movies[2]].Poster.values[0]

    if len(data[data.Title == movies[3]].Poster.values) == 0:
        link4 = 'https://as2.ftcdn.net/jpg/01/23/50/75/500_F_123507588_WM22wAfkxrFwuNzHvxejP3AxnQTGCvIY.jpg'
    else:
        link4 = data[data.Title == movies[3]].Poster.values[0]

    if len(data[data.Title == movies[4]].Poster.values) == 0:
        link5 = 'https://as2.ftcdn.net/jpg/01/23/50/75/500_F_123507588_WM22wAfkxrFwuNzHvxejP3AxnQTGCvIY.jpg'
    else:
        link5 = data[data.Title == movies[4]].Poster.values[0]

    if len(data[data.Title == movies[5]].Poster.values) == 0:
        link6 = 'https://as2.ftcdn.net/jpg/01/23/50/75/500_F_123507588_WM22wAfkxrFwuNzHvxejP3AxnQTGCvIY.jpg'
    else:
        link6 = data[data.Title == movies[5]].Poster.values[0]

    if len(data[data.Title == movies[6]].Poster.values) == 0:
        link7 = 'https://as2.ftcdn.net/jpg/01/23/50/75/500_F_123507588_WM22wAfkxrFwuNzHvxejP3AxnQTGCvIY.jpg'
    else:
        link7 = data[data.Title == movies[6]].Poster.values[0]

    if len(data[data.Title == movies[7]].Poster.values) == 0:
        link8 = 'https://as2.ftcdn.net/jpg/01/23/50/75/500_F_123507588_WM22wAfkxrFwuNzHvxejP3AxnQTGCvIY.jpg'
    else:
        link8 = data[data.Title == movies[7]].Poster.values[0]

    return render(request,'blog/index.html',context = {'movie1': movies[0], 'movie2': movies[1], 'movie3': movies[2]
        , 'movie4': movies[3], 'movie5': movies[4], 'movie6': movies[5], 'movie7': movies[6], 'movie8': movies[7],
                              'link1':link1,'link2':link2,'link3':link3,'link4':link4,'link5':link5,'link6':link6,
                              'link7': link7,'link8':link8})



def recommend(request):
    df = pd.read_csv(r'C:\Users\Kaan\Desktop\django_blog\blog\movie_dataset.csv')
    data = pd.read_csv(r'C:\Users\Kaan\Desktop\django_blog\blog\main.csv' , encoding='latin1')

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

    movie_user_likes = request.GET['movie_name']
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

    if len(data[data.Title == movies[0]].Poster.values) == 0:
        link1 = 'https://as2.ftcdn.net/jpg/01/23/50/75/500_F_123507588_WM22wAfkxrFwuNzHvxejP3AxnQTGCvIY.jpg'
    else:
        link1 = data[data.Title == movies[0]].Poster.values[0]

    if len(data[data.Title == movies[1]].Poster.values) == 0:
        link2 = 'https://as2.ftcdn.net/jpg/01/23/50/75/500_F_123507588_WM22wAfkxrFwuNzHvxejP3AxnQTGCvIY.jpg'
    else:
        link2 = data[data.Title == movies[1]].Poster.values[0]

    if len(data[data.Title == movies[2]].Poster.values) == 0:
        link3 = 'https://as2.ftcdn.net/jpg/01/23/50/75/500_F_123507588_WM22wAfkxrFwuNzHvxejP3AxnQTGCvIY.jpg'
    else:
        link3 = data[data.Title == movies[2]].Poster.values[0]

    if len(data[data.Title == movies[3]].Poster.values) == 0:
        link4 = 'https://as2.ftcdn.net/jpg/01/23/50/75/500_F_123507588_WM22wAfkxrFwuNzHvxejP3AxnQTGCvIY.jpg'
    else:
        link4 = data[data.Title == movies[3]].Poster.values[0]

    if len(data[data.Title == movies[4]].Poster.values) == 0:
        link5 = 'https://as2.ftcdn.net/jpg/01/23/50/75/500_F_123507588_WM22wAfkxrFwuNzHvxejP3AxnQTGCvIY.jpg'
    else:
        link5 = data[data.Title == movies[4]].Poster.values[0]

    if len(data[data.Title == movies[5]].Poster.values) == 0:
        link6 = 'https://as2.ftcdn.net/jpg/01/23/50/75/500_F_123507588_WM22wAfkxrFwuNzHvxejP3AxnQTGCvIY.jpg'
    else:
        link6 = data[data.Title == movies[5]].Poster.values[0]

    if len(data[data.Title == movies[6]].Poster.values) == 0:
        link7 = 'https://as2.ftcdn.net/jpg/01/23/50/75/500_F_123507588_WM22wAfkxrFwuNzHvxejP3AxnQTGCvIY.jpg'
    else:
        link7 = data[data.Title == movies[6]].Poster.values[0]

    if len(data[data.Title == movies[7]].Poster.values) == 0:
        link8 = 'https://as2.ftcdn.net/jpg/01/23/50/75/500_F_123507588_WM22wAfkxrFwuNzHvxejP3AxnQTGCvIY.jpg'
    else:
        link8 = data[data.Title == movies[7]].Poster.values[0]




    return JsonResponse(data={'movie1': movies[0], 'movie2': movies[1], 'movie3': movies[2]
        , 'movie4': movies[3], 'movie5': movies[4], 'movie6': movies[5], 'movie7': movies[6], 'movie8': movies[7],
                              'link1':link1,'link2':link2,'link3':link3,'link4':link4,'link5':link5,'link6':link6,
                              'link7': link7,'link8':link8,})


def movie_page(request):
    new_data = pd.DataFrame()
    movie_name = request.POST['movie__1']
    new_data = df[df.title == movie_name]
    return render(request,'blog/movie_page.html',context={"title":new_data['title'].values[0] , "genres":new_data['genres'].values[0] ,
                                                          "overview":new_data['overview'].values[0],
                                                          "release_date":new_data['release_date'].values[0],
                                                          "runtime":new_data['runtime'].values[0] ,
                                                          "vote_average":new_data['vote_average'].values[0],
                                                          "director":new_data['director'].values[0] ,
                                                          "homepage":new_data['homepage'].values[0]})