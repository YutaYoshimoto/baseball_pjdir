from django.db import models
from django.utils import timezone
from django.db.models import Q
from django.contrib.auth import get_user, get_user_model

User = get_user_model()
        #qs = qs.filter(public=True) 
    
class NippoModelQuerySet(models.QuerySet):
    def search(self, query=None):
        qs = self
        if query is not None:
            or_lookup = (
                Q(date__icontains=query)|
                Q(team__icontains=query)|
                Q(district__icontains=query)|
                Q(content__icontains=query)| 
                Q(grade__icontains=query)            
            )
            qs = qs.filter(or_lookup).distinct()
        return qs.order_by("-timestamp") 
class NippoModelManager(models.Manager):
    def get_queryset(self):
        return NippoModelQuerySet(self.model, using=self._db)

    def search(self, query=None):
        return self.get_queryset().search(query=query)
class NippoModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(verbose_name='予定日', blank=True, null=True,default=timezone.now)#年月日、初期値入力日
    team = models.CharField(verbose_name='チーム名',max_length=100,default='チーム名')#タイトル
    grade = models.CharField(verbose_name='年齢層：小学生,中学生,高校生,社会人',max_length=100,default='小学生')#タイトル
    district = models.CharField(verbose_name='地区',max_length=100,default='地区')#内容
    content = models.TextField(verbose_name='内容',default='詳細な内容')#内容
    timestamp = models.DateTimeField(auto_now_add=True)
    objects = NippoModelManager()
class ImageUpload(models.Model):
    title = models.CharField(max_length=100,default='default-title')
    img = models.ImageField(upload_to="images")

    def __str__(self):
        return self.title    
    #public = models.BooleanField(default=False, verbose_name="公開する")
    #slug = models.SlugField(null=True, blank=True)