from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length = 100 ,verbose_name = 'Baslik Giriniz' , help_text = 'Baslik Bilgisi Burada Girilir' , blank=False , null=True, )
    icerik = models.TextField(max_length = 1000 , verbose_name = 'Icerik Giriniz',null=True , blank=False)
    created_date = models.DateField(auto_now_add=True)