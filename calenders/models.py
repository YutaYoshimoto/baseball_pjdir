from django.db import models
from django.utils import timezone
from django.db.models import Q
from django.contrib.auth import get_user, get_user_model

User = get_user_model()

    
class NippoModelQuerySet(models.QuerySet):
    def search(self, query=None):
        qs = self
        #qs = qs.filter(public=True) #公開済みの日報のみでQuerySetを作成しています
        if query is not None:
            or_lookup = (
                Q(date__icontains=query)|
                Q(team__icontains=query)|
                Q(district__icontains=query)|
                Q(content__icontains=query)            
            )
            qs = qs.filter(or_lookup).distinct()
        return qs.order_by("-timestamp") #新しい順に並び替えてます
class NippoModelManager(models.Manager):
    def get_queryset(self):
        return NippoModelQuerySet(self.model, using=self._db)

    def search(self, query=None):
        return self.get_queryset().search(query=query)
    
class ImageUpload(models.Model):
    title = models.CharField(max_length=100,default='default-title')
    img = models.ImageField(upload_to="images")

    def __str__(self):
        return self.title
    
class NippoModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(verbose_name='日付', blank=True, null=True,default=timezone.now)#年月日、初期値入力日
    team = models.CharField(verbose_name='チーム名',max_length=100,default='チーム名')#タイトル
    district = models.CharField(verbose_name='地区',max_length=100,default='地区')#内容
    content = models.TextField(verbose_name='内容',default='default-content')#内容
    timestamp = models.DateTimeField(auto_now_add=True)
    objects = NippoModelManager()
    #public = models.BooleanField(default=False, verbose_name="公開する")
    #slug = models.SlugField(null=True, blank=True)