from django.contrib import admin
from .models import NippoModel,ImageUpload #追記

admin.site.register(NippoModel) #追記
admin.site.register(ImageUpload)