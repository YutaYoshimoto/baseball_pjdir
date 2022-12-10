from django.db import models
from django.utils import timezone

class NippoModel(models.Model):
    #date = models.DateField('日付', blank=True, null=True,default=timezone.now)#年月日、初期値入力日
    title = models.CharField(max_length=100,default='default-title')#タイトル
    #content = models.CharField(max_length=1000,default='default-contet')
    content = models.TextField( verbose_name='default-contet')#内容
    timestamp = models.DateTimeField(auto_now_add=True)
    
    #public = models.BooleanField(default=False, verbose_name="公開する")
    #slug = models.SlugField(max_length=20, unique=True, default=slug_maker)
    
    def __str__(self):
        return self.title
    
class ImageUpload(models.Model):
    title = models.CharField(max_length=100,default='default-title')
    img = models.ImageField(upload_to="images")

    def __str__(self):
        return self.title