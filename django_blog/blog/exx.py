import pandas as pd
df = pd.read_csv(r'C:\Users\Kaan\Desktop\django_blog\blog\movie_dataset.csv')

data = pd.read_csv(r'C:\Users\Kaan\Desktop\django_blog\blog\main.csv' , encoding='latin1')

movies = ['Superman' , 'Batman']

if len(data[data.Title == movies[0]].Poster.values) == 0:
    link1 = 'https://as2.ftcdn.net/jpg/01/23/50/75/500_F_123507588_WM22wAfkxrFwuNzHvxejP3AxnQTGCvIY.jpg'
else:
    link1 = data[data.Title == movies[0]].Poster.values[0]

print(link1)
