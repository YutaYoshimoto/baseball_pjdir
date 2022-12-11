from django.shortcuts import render,get_object_or_404,redirect
from random import randint
from .models import NippoModel
from .forms import ImageUploadForm,NippoModelForm
from django.views.generic.edit import CreateView
from django.views.generic import ListView,DetailView,FormView,DeleteView,UpdateView
from django.urls import reverse, reverse_lazy

class NippoDetailView(DetailView):
    template_name = "nippo/nippo-detail.html"
    def get_queryset(self):
        return  NippoModel.objects.all()   
      
 
    
class NippoListView(ListView):
    template_name = "nippo/nippo-list.html"
    def get_queryset(self):
        try:
            q = self.request.GET["search"]
        except:
            q = None
        return NippoModel.objects.search(query=q)
class NippoCreateFormView(FormView):
    template_name = "nippo/nippo-formclass.html"
    form_class = NippoModelForm
    success_url = reverse_lazy("nippo-list")

    def form_valid(self, form):
        data = form.cleaned_data
        obj = NippoModel(**data)
        obj.save()
        return super().form_valid(form)

class NippoUpdateFormView(UpdateView):
    template_name = "nippo/nippo-formclass.html"
    model = NippoModel
    form_class = NippoModelForm
    success_url = reverse_lazy("nippo-list")

class NippoDeleteView(DeleteView):
    template_name = "nippo/nippo-delete.html"
    model = NippoModel
    success_url = reverse_lazy("nippo-list")

class ImageUploadView(CreateView):
    template_name = "nippo/image-upload.html"
    form_class = ImageUploadForm
    success_url = "/"
    
def get_queryset(self):
    try:
        q = self.request.GET["search"]
    except:
        q = None
    return NippoModel.objects.search(query=q)

'''
class NippoCreateFormView(CreateView):
    template_name = "nippo/nippo-formclass.html"
    form_class = NippoModelForm
    success_url = reverse_lazy("nippo-list")
'''