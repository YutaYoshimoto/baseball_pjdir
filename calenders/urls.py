from django.urls import path
from .views import ImageUploadView
from .views import NippoListView, NippoCreateFormView, NippoDeleteView,NippoUpdateFormView ,NippoDetailView
from .views import NippoReqestDetailView, reqest_mail
 
urlpatterns = [
  path("", NippoListView.as_view(), name="nippo-list"),
  path("detail/<int:pk>", NippoDetailView.as_view(), name="nippo-detail"), 
  path("create/", NippoCreateFormView.as_view(),name="nippo-create"),
  path("update/<int:pk>/", NippoUpdateFormView.as_view(), name="nippo-update"),
  path("delete/<int:pk>/", NippoDeleteView.as_view(), name="nippo-delete"),
  path("image-upload/", ImageUploadView.as_view(), name="image-upload"),
  path("reqest/<int:pk>/", NippoReqestDetailView, name="nippo-reqest"),
  path("reqest_mail/<int:pk>/", reqest_mail, name="reqest-mail"),
  #path("", nippoListView,name="nippo-list"), #クラス作成前の関数版
  #path("detail/", nippoDetailView)
  #path("create/", nippoCreateFormView, name="nippo-create"),
  #path("update/<slug:slug>/", NippoCreateView.as_view(), name="nippo-update"),
  #path("update/", nippoUpdateFormView, name="nippo-update"),
]