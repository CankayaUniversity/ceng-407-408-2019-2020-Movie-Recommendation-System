from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.http import JsonResponse

import pandas as pd
import numpy as np # pip install numpy==1.16.1
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import random
import statistics
import time
from.models import userLiked
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm






def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return render(response, "blog/success_message.html")
        
    else:
        form = RegisterForm()
    return render(response, "blog/register.html", {"form": form})




df = pd.read_csv("blog/movie_dataset.csv")
data = pd.read_csv("blog/main.csv", encoding='latin1')



def post_list(request):
    df = pd.read_csv("blog/movie_dataset.csv")
    data = pd.read_csv("blog/main.csv", encoding='latin1')
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
    movies = []
    while len(movies) != 8:
        number = random.randrange(0, 4500)
        if "&" not in df.loc[number].title:
            movies.append(df.loc[number].title)


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

    if request.user.is_authenticated == True and userLiked.objects.filter(username=request.user.username).all().count() >= 8:
        movies1 = userLiked.objects.filter(username=request.user.username).values_list('liked_movie', flat=True)

        temp_movie1 = []
        for i in range(0, 8):
            temp_movie1.append(str(movies1[i]))

        yesno_list = [0,0,0,0,0,0,0,0]
        for i in range(0,8):
            for j in range(0,8):
                if movies[i] == temp_movie1[j]:
                    yesno_list[i] = 1

        number_movies = userLiked.objects.filter(username=request.user.username).values_list('liked_movie', flat=True)
        number_movies_len = len(number_movies)

        return render(request,'blog/index.html',context = {'movie1': movies[0], 'movie2': movies[1], 'movie3': movies[2]
            , 'movie4': movies[3], 'movie5': movies[4], 'movie6': movies[5], 'movie7': movies[6], 'movie8': movies[7],
                                  'link1':link1,'link2':link2,'link3':link3,'link4':link4,'link5':link5,'link6':link6,
                                  'link7': link7,'link8':link8 , 'yesno_movie1' : yesno_list[0],
                                                           'yesno_movie2': yesno_list[1],'yesno_movie3' : yesno_list[2]
                                                           ,'yesno_movie4' : yesno_list[3],'yesno_movie5' : yesno_list[4]
                                                           ,'yesno_movie6' : yesno_list[5],'yesno_movie7' : yesno_list[6],
                                                           'yesno_movie8': yesno_list[7] , 'movies_number':number_movies_len})
    else:
        return render(request,'blog/index.html',context = {'movie1': movies[0], 'movie2': movies[1], 'movie3': movies[2]
            , 'movie4': movies[3], 'movie5': movies[4], 'movie6': movies[5], 'movie7': movies[6], 'movie8': movies[7],
                                  'link1':link1,'link2':link2,'link3':link3,'link4':link4,'link5':link5,'link6':link6,
                                  'link7': link7,'link8':link8})
            

def pagenumber(request):
    pagenumber = int(request.GET['pagenumber'])

    df = pd.read_csv("blog/movie_dataset.csv")
    data = pd.read_csv("blog/main.csv", encoding='latin1')

    category = request.GET['category']
    category = str(category)

    # category = "Horror"

    new_df = pd.DataFrame()
    new_df = df[df.genres.str.contains(category) == True]

    movie_list = []  # kategoriye ait film listesi burada
    for i in new_df.title:
        movie_list.append(i)

    movies = []
    for i in range((pagenumber -1) * 8, pagenumber * 8):
        movies.append(movie_list[i])

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
                              'link1': link1, 'link2': link2, 'link3': link3, 'link4': link4, 'link5': link5,
                              'link6': link6,
                              'link7': link7, 'link8': link8})

    return JsonResponse(data={'name': movie_list})

def recommend(request):
    movie_user_likes = str(request.GET['movie_name']).capitalize()

    df = pd.read_csv("blog/movie_dataset.csv")
    data = pd.read_csv("blog/main.csv", encoding='latin1')

    def word2vec(word):
        from collections import Counter
        from math import sqrt

        # count the characters in word
        cw = Counter(word)
        # precomputes a set of the different characters
        sw = set(cw)
        # precomputes the "length" of the word vector
        lw = sqrt(sum(c * c for c in cw.values()))

        # return a tuple
        return cw, sw, lw

    def cosdis(v1, v2):
        # which characters are common to the two words?
        common = v1[1].intersection(v2[1])
        # by definition of cosine distance we have
        return sum(v1[0][ch] * v2[0][ch] for ch in common) / v1[2] / v2[2]

    movie_user_likes = word2vec(movie_user_likes)

    title = df.title.tolist()
    title_df = pd.DataFrame(columns=['title', 'sim'])
    temp_title_list = []
    temp_sim = []

    for i in title:
        temp_title_list.append(i)
        i = word2vec(i)
        temp_sim.append(cosdis(movie_user_likes, i))

    title_df.title = temp_title_list
    title_df.sim = temp_sim

    new_list = title_df.sort_values(by='sim', ascending=False)
    new_list = new_list.reset_index()
    movie_user_likes = new_list.title[0]


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

    if len(data[data.Title == movie_user_likes].Poster.values) == 0:
        link1 = 'https://as2.ftcdn.net/jpg/01/23/50/75/500_F_123507588_WM22wAfkxrFwuNzHvxejP3AxnQTGCvIY.jpg'
    else:
        link1 = data[data.Title == movie_user_likes].Poster.values[0]

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

    movies1 = userLiked.objects.filter(username=request.user.username).values_list('liked_movie', flat=True)


    temp_movie1 = [] ## databasede begenilen filmler
    for i in range(0, len(movies1)):
        temp_movie1.append(str(movies1[i]))

    yesno_list = [0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(0,len(temp_movie1)):
        if movie_user_likes == temp_movie1[i]:
            yesno_list[0] = 1



    for i in range(1, 8):
        for j in range(0,len(temp_movie1)):
            if movies[i] == temp_movie1[j]:
                yesno_list[i] = 1





    return JsonResponse(data={'movie1': movie_user_likes, 'movie2': movies[1], 'movie3': movies[2]
        , 'movie4': movies[3], 'movie5': movies[4], 'movie6': movies[5], 'movie7': movies[6], 'movie8': movies[7],
          'link1':link1,'link2':link2,'link3':link3,'link4':link4,'link5':link5,'link6':link6,
          'link7': link7,'link8':link8, 'yesno_movie1' : yesno_list[0],  
          'yesno_movie2': yesno_list[1],'yesno_movie3' : yesno_list[2]  
               ,'yesno_movie4' : yesno_list[3],'yesno_movie5' : yesno_list[4],'yesno_movie6' : yesno_list[5],'yesno_movie7' : yesno_list[6],   
                 'yesno_movie8': yesno_list[7] , 'alllist' : yesno_list , 'temp_movie1' : temp_movie1 , 'movies':movies})







def movie_page(request):
    new_data = pd.DataFrame()
    movie_name = request.POST['movie_text']

    if data[data.Title == movie_name].values.any() == 0:
        new_data = df[df.title == movie_name]
    else:
        new_data = data[data.title == movie_name]

    if len(data[data.Title == movie_name].Poster.values) == 0:
        link = 'https://as2.ftcdn.net/jpg/01/23/50/75/500_F_123507588_WM22wAfkxrFwuNzHvxejP3AxnQTGCvIY.jpg'
    else:
        link = data[data.Title == movie_name].Poster.values[0]

    return render(request,'blog/movie_page.html',context={"title":new_data['title'].values[0] , "genres":new_data['genres'].values[0] ,
                                                          "overview":new_data['overview'].values[0],
                                                          "release_date":new_data['release_date'].values[0],
                                                          "runtime":new_data['runtime'].values[0] ,
                                                          "vote_average":new_data['vote_average'].values[0],
                                                          "director":new_data['director'].values[0] ,
                                                          "homepage":new_data['homepage'].values[0] , 'link':link})




def movie_liked(request):
      movie_name = request.GET['movie_name']
      flag = 0

      movies1 = userLiked.objects.filter(username=request.user.username).values_list('liked_movie', flat=True)

      temp_movie1 = []  ## databasede begenilen filmler
      for i in range(0, len(movies1)):
          temp_movie1.append(str(movies1[i]))

      for i in range(0,len(temp_movie1)):
          if movie_name == temp_movie1[i]:
              flag = 1


      if flag == 0:
          newMovieLiked = userLiked(username=request.user.get_username(), liked_movie=movie_name)
          newMovieLiked.save()
      elif flag == 1:
          newMovieLiked = userLiked.objects.get(username=request.user.get_username(), liked_movie=movie_name)
          newMovieLiked.delete()

      return JsonResponse(data={'flag': flag })










def buttonRefresh(request):
    df = pd.read_csv("blog/movie_dataset.csv")
    data = pd.read_csv("blog/main.csv", encoding='latin1')
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
    movies = []
    for i in range(0,8):
        number = random.randrange(0, 4500)
        movies.append(df.loc[number].title)


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
                              'link7': link7,'link8':link8})

                                            # Get Recommendation Page

def getrecommendations(request):
    movies = userLiked.objects.filter(username=request.user.username).values_list('liked_movie' , flat=True)

    movie_list = []
    link_list = []

    for i in range(0,8):

        df = pd.read_csv("blog/movie_dataset.csv")
        data = pd.read_csv("blog/main.csv", encoding='latin1')
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

        movie_user_likes = str(movies[i])
        movie_index = get_index_from_title(movie_user_likes)
        similar_movies = list(enumerate(cosine_sim[movie_index]))

        sorted_similar_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)[1:]

        i = 0
        moviess = []
        for element in sorted_similar_movies:
            moviess.append(get_title_from_index(element[0]))
            i = i + 1
            if i > 10:
                break


        if len(data[data.Title == moviess[1]].Poster.values) == 0:
            link = 'https://as2.ftcdn.net/jpg/01/23/50/75/500_F_123507588_WM22wAfkxrFwuNzHvxejP3AxnQTGCvIY.jpg'
        else:
            link = data[data.Title == moviess[1]].Poster.values[0]

        movie_list.append(moviess[1])
        link_list.append(link)



    return render(request , 'blog/getrecommendation.html' , context={'movie1': movie_list[0], 'movie2': movie_list[1], 'movie3': movie_list[2]
        , 'movie4': movie_list[3], 'movie5': movie_list[4], 'movie6': movie_list[5], 'movie7': movie_list[6], 'movie8': movie_list[7],
                              'link1': link_list[0], 'link2': link_list[1], 'link3': link_list[2], 'link4': link_list[3], 'link5': link_list[4],
                              'link6': link_list[5],
                              'link7': link_list[6], 'link8': link_list[7]})




                                                    #User Similarities

def friend_similarity(request):
    movies1 = userLiked.objects.filter(username='admin').values_list('liked_movie', flat=True)
    movies2 = userLiked.objects.filter(username='adminadmin').values_list('liked_movie', flat=True)

    #admin
    temp_movie1 = []
    for i in range(0,8):
        temp_movie1.append(str(movies1[i]))

    #adminadmin
    temp_movie2 = []
    for i in range(0,8):
        temp_movie2.append(str(movies2[i]))




    df = pd.read_csv("blog/movie_dataset.csv")
    data = pd.read_csv("blog/main.csv", encoding='latin1')
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



    similarity_movies = []

    for movie_temp_1 in temp_movie1:

        movie_user_likes = str(movie_temp_1)
        movie_index = get_index_from_title(movie_user_likes)
        similar_movies = list(enumerate(cosine_sim[movie_index]))
        sorted_similar_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)[1:]

        for movie_temp_2 in temp_movie2:

            moviess = []
            for element in similar_movies:
                moviess.append(get_title_from_index(element[0]))

            index = get_index_from_title(str(movie_temp_2))

            for q in sorted_similar_movies:
                    if q[0] == index:
                        similarity_movies.append(q[1])
                        break




    return JsonResponse(data={'movie1': get_title_from_index(2433) , 'movie2':similarity_movies , 'movie3' : len(similarity_movies) , 'movie4' : statistics.mean(similarity_movies)})


def movie_category(request):
    df = pd.read_csv("blog/movie_dataset.csv")
    data = pd.read_csv("blog/main.csv", encoding='latin1')

    category = request.GET['movie_cat']
    category = str(category)

    new_df = pd.DataFrame()
    new_df = df[df.genres.str.contains(category) == True]

    movie_list = [] # kategoriye ait film listesi burada
    for i in new_df.title:
        movie_list.append(i)

    movies = []
    for i in range(0, 8):
        movies.append(movie_list[i])

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
                              'link1': link1, 'link2': link2, 'link3': link3, 'link4': link4, 'link5': link5,
                              'link6': link6,
                              'link7': link7, 'link8': link8})




    return JsonResponse(data={'name':movie_list})

def movieofuser(request):
    movies1 = userLiked.objects.filter(username=request.user.username).values_list('liked_movie', flat=True)

    movies = []  ## databasede begenilen filmler
    for i in range(0, len(movies1)):
        movies.append(str(movies1[i]))

    if len(movies) == 1:
        return JsonResponse(data={'size':len(movies),'movie1': movies[0]})
    elif len(movies) == 2:
        return JsonResponse(data={'size': len(movies), 'movie1': movies[0] , 'movie2':movies[1]})


    elif len(movies) == 3:
        return JsonResponse(data={'size': len(movies), 'movie1': movies[0], 'movie2': movies[1], 'movie3': movies[2]})
    elif len(movies) == 4:
        return JsonResponse(data={'size': len(movies), 'movie1': movies[0], 'movie2': movies[1], 'movie3': movies[2],
                                  'movie4': movies[3],
                                  })
    elif len(movies) == 5:
        return JsonResponse(data={'size': len(movies), 'movie1': movies[0], 'movie2': movies[1], 'movie3': movies[2],
                                  'movie4': movies[3],
                                  'movie5': movies[4] })


    elif len(movies) == 6:
        return JsonResponse(data={'size': len(movies), 'movie1': movies[0], 'movie2': movies[1], 'movie3': movies[2],
                                  'movie4': movies[3],
                                  'movie5': movies[4], 'movie6': movies[5]})
    elif len(movies) == 7:
        return JsonResponse(data={'size': len(movies), 'movie1': movies[0], 'movie2': movies[1], 'movie3': movies[2],
                                  'movie4': movies[3],
                                  'movie5': movies[4], 'movie6': movies[5], 'movie7': movies[6],  })
    elif len(movies) == 8:
        return JsonResponse(data={'size': len(movies), 'movie1': movies[0], 'movie2': movies[1], 'movie3': movies[2],
                                  'movie4': movies[3],
                                  'movie5': movies[4], 'movie6': movies[5], 'movie7': movies[6], 'movie8': movies[7], })
    elif len(movies) == 9:
        return JsonResponse(data={'size': len(movies), 'movie1': movies[0], 'movie2': movies[1], 'movie3': movies[2],
                                  'movie4': movies[3],
                                  'movie5': movies[4], 'movie6': movies[5], 'movie7': movies[6], 'movie8': movies[7],
                                  'movie9': movies[8] })
    elif len(movies) == 10:
        return JsonResponse(data={'size': len(movies), 'movie1': movies[0], 'movie2': movies[1], 'movie3': movies[2],
                                  'movie4': movies[3],
                                  'movie5': movies[4], 'movie6': movies[5], 'movie7': movies[6], 'movie8': movies[7],
                                  'movie9': movies[8],
                                  'movie10': movies[9] })
    elif len(movies) == 11:
        return JsonResponse(data={'size': len(movies), 'movie1': movies[0], 'movie2': movies[1], 'movie3': movies[2],
                                  'movie4': movies[3],
                                  'movie5': movies[4], 'movie6': movies[5], 'movie7': movies[6], 'movie8': movies[7],
                                  'movie9': movies[8],
                                  'movie10': movies[9], 'movie11': movies[10] })
    elif len(movies) == 12:
        return JsonResponse(data={'size': len(movies), 'movie1': movies[0], 'movie2': movies[1], 'movie3': movies[2],
                                  'movie4': movies[3],
                                  'movie5': movies[4], 'movie6': movies[5], 'movie7': movies[6], 'movie8': movies[7],
                                  'movie9': movies[8],
                                  'movie10': movies[9], 'movie11': movies[10], 'movie12': movies[11]})
    elif len(movies) == 13:
        return JsonResponse(data={'size': len(movies), 'movie1': movies[0], 'movie2': movies[1], 'movie3': movies[2],
                                  'movie4': movies[3],
                                  'movie5': movies[4], 'movie6': movies[5], 'movie7': movies[6], 'movie8': movies[7],
                                  'movie9': movies[8],
                                  'movie10': movies[9], 'movie11': movies[10], 'movie12': movies[11],
                                  'movie13': movies[12] })
    elif len(movies) == 14:
        return JsonResponse(data={'size': len(movies), 'movie1': movies[0], 'movie2': movies[1], 'movie3': movies[2],
                                  'movie4': movies[3],
                                  'movie5': movies[4], 'movie6': movies[5], 'movie7': movies[6], 'movie8': movies[7],
                                  'movie9': movies[8],
                                  'movie10': movies[9], 'movie11': movies[10], 'movie12': movies[11],
                                  'movie13': movies[12],
                                  'movie14': movies[13],
                                  })
    elif len(movies) == 15:
        return JsonResponse(data={'size': len(movies), 'movie1': movies[0], 'movie2': movies[1], 'movie3': movies[2],
                                  'movie4': movies[3],
                                  'movie5': movies[4], 'movie6': movies[5], 'movie7': movies[6], 'movie8': movies[7],
                                  'movie9': movies[8],
                                  'movie10': movies[9], 'movie11': movies[10], 'movie12': movies[11],
                                  'movie13': movies[12],
                                  'movie14': movies[13],
                                  'movie15': movies[14]})
    elif len(movies) == 16:
        return JsonResponse(data={'size': len(movies), 'movie1': movies[0], 'movie2': movies[1], 'movie3': movies[2],
                                  'movie4': movies[3],
                                  'movie5': movies[4], 'movie6': movies[5], 'movie7': movies[6], 'movie8': movies[7],
                                  'movie9': movies[8],
                                  'movie10': movies[9], 'movie11': movies[10], 'movie12': movies[11],
                                  'movie13': movies[12],
                                  'movie14': movies[13],
                                  'movie15': movies[14], 'movie16': movies[15]})
    elif len(movies) == 17:
        return JsonResponse(data={'size': len(movies), 'movie1': movies[0], 'movie2': movies[1], 'movie3': movies[2],
                                  'movie4': movies[3],
                                  'movie5': movies[4], 'movie6': movies[5], 'movie7': movies[6], 'movie8': movies[7],
                                  'movie9': movies[8],
                                  'movie10': movies[9], 'movie11': movies[10], 'movie12': movies[11],
                                  'movie13': movies[12],
                                  'movie14': movies[13],
                                  'movie15': movies[14], 'movie16': movies[15], 'movie17': movies[16]})
    elif len(movies) == 18:
        return JsonResponse(data={'size': len(movies), 'movie1': movies[0], 'movie2': movies[1], 'movie3': movies[2],
                                  'movie4': movies[3],
                                  'movie5': movies[4], 'movie6': movies[5], 'movie7': movies[6], 'movie8': movies[7],
                                  'movie9': movies[8],
                                  'movie10': movies[9], 'movie11': movies[10], 'movie12': movies[11],
                                  'movie13': movies[12],
                                  'movie14': movies[13],
                                  'movie15': movies[14], 'movie16': movies[15], 'movie17': movies[16],
                                  'movie18': movies[17], })
    elif len(movies) == 19:
        return JsonResponse(data={'size': len(movies), 'movie1': movies[0], 'movie2': movies[1], 'movie3': movies[2],
                                  'movie4': movies[3],
                                  'movie5': movies[4], 'movie6': movies[5], 'movie7': movies[6], 'movie8': movies[7],
                                  'movie9': movies[8],
                                  'movie10': movies[9], 'movie11': movies[10], 'movie12': movies[11],
                                  'movie13': movies[12],
                                  'movie14': movies[13],
                                  'movie15': movies[14], 'movie16': movies[15], 'movie17': movies[16],
                                  'movie18': movies[17],
                                  'movie19': movies[18] })
    elif len(movies) == 20:
        return JsonResponse(data={'size': len(movies), 'movie1': movies[0], 'movie2': movies[1], 'movie3': movies[2],
                                  'movie4': movies[3],
                                  'movie5': movies[4], 'movie6': movies[5], 'movie7': movies[6], 'movie8': movies[7],
                                  'movie9': movies[8],
                                  'movie10': movies[9], 'movie11': movies[10], 'movie12': movies[11],
                                  'movie13': movies[12],
                                  'movie14': movies[13],
                                  'movie15': movies[14], 'movie16': movies[15], 'movie17': movies[16],
                                  'movie18': movies[17],
                                  'movie19': movies[18],
                                  'movie20': movies[19]})





def like_or_dislike(request):
    movie_name = request.GET['movie_name']
    flag = 0

    movies1 = userLiked.objects.filter(username=request.user.username).values_list('liked_movie', flat=True)

    temp_movie1 = []  ## databasede begenilen filmler
    for i in range(0, len(movies1)):
        temp_movie1.append(str(movies1[i]))

    for i in range(0, len(temp_movie1)):
        if movie_name == temp_movie1[i]:
            flag = 1

    return JsonResponse(data={'flag': flag})

def new_recommend(request):
    movies = userLiked.objects.filter(username=request.user.username).values_list('liked_movie', flat=True)

    movie_list = []
    link_list = []

    for i in range(0, len(movies)):

        df = pd.read_csv("blog/movie_dataset.csv")
        data = pd.read_csv("blog/main.csv", encoding='latin1')
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

        movie_user_likes = str(movies[i])
        movie_index = get_index_from_title(movie_user_likes)
        similar_movies = list(enumerate(cosine_sim[movie_index]))

        sorted_similar_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)[1:]

        i = 0
        moviess = []
        for element in sorted_similar_movies:
            moviess.append(get_title_from_index(element[0]))
            i = i + 1
            if i > 10:
                break

        if len(data[data.Title == moviess[1]].Poster.values) == 0:
            link = 'https://as2.ftcdn.net/jpg/01/23/50/75/500_F_123507588_WM22wAfkxrFwuNzHvxejP3AxnQTGCvIY.jpg'
        else:
            link = data[data.Title == moviess[1]].Poster.values[0]

        movie_list.append(moviess[1])
        link_list.append(link)

    random_list = []

    while len(random_list) != 8:
        number = random.randrange(0, len(movie_list))
        if number not in random_list:
            random_list.append(number)



    return JsonResponse(data={'recom_movie1': movie_list[random_list[0]], 'recom_movie2': movie_list[random_list[1]], 'recom_movie3': movie_list[random_list[2]]
        , 'recom_movie4': movie_list[random_list[3]], 'recom_movie5': movie_list[random_list[4]], 'recom_movie6': movie_list[random_list[5]], 'recom_movie7': movie_list[random_list[6]],
                              'recom_movie8': movie_list[random_list[7]]})