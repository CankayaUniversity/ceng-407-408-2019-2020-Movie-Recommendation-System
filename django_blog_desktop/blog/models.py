from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length = 100 ,verbose_name = 'Baslik Giriniz' , help_text = 'Baslik Bilgisi Burada Girilir' , blank=False , null=True, )
    icerik = models.TextField(max_length = 1000 , verbose_name = 'Icerik Giriniz',null=True , blank=False)
    created_date = models.DateField(auto_now_add=True)



class userLiked(models.Model):
    user_id = models.IntegerField(primary_key=True)
    username= models.CharField(max_length=100)
    liked_movie= models.CharField(max_length=100)



class comment(models.Model):
    comment_id = models.IntegerField(primary_key=True)
    username= models.CharField(max_length=100)
    comment= models.TextField(max_length=500)


class friend(models.Model):
    friend_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=100)
    friend_username = models.CharField(max_length=100)
