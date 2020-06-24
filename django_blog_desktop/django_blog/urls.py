"""django_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from blog import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/',views.post_list , name='post_list') ,
    path('recommend/',views.recommend , name='recommend'),
    path('movie_page',views.movie_page , name='movie_page'),
    path('register/', views.register, name='register'),
    path('movie_liked/', views.movie_liked, name='movie_liked'),
    path('buttonRefresh/', views.buttonRefresh, name='buttonRefresh'),
    path('getrecommendation/', views.getrecommendations, name='getrecommendations'),
    path('',include("django.contrib.auth.urls")),
    path('friendsimilarity/', views.friend_similarity, name='friendsimilarity'),
    path('movie_category/', views.movie_category, name='movie_category'),
    path('new_recommend/', views.new_recommend, name='new_recommend'),
    path('like_or_dislike/', views.like_or_dislike, name='like_or_dislike'),
    path('movieofuser/', views.movieofuser, name='movieofuser'),
    path('pagenumber/', views.pagenumber, name='pagenumber'),
    path('', include("django.contrib.auth.urls")),


]

urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
