from django.shortcuts import render,get_object_or_404,redirect
from random import randint
from .models import NippoModel
from .forms import ImageUploadForm,NippoModelForm
from django.views.generic.edit import CreateView
from django.views.generic import ListView,DetailView,FormView,DeleteView,UpdateView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.decorators import user_passes_test
from django.core.mail import EmailMultiAlternatives


class OwnerOnly(UserPassesTestMixin):
    def test_func(self):
        nippo_instance = self.get_object()
        return nippo_instance.user == self.request.user
    
    def handle_no_permission(self):
        return redirect("nippo-detail", pk=self.kwargs["pk"])
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
class NippoCreateFormView(LoginRequiredMixin,FormView):
    template_name = "nippo/nippo-formclass.html"
    form_class = NippoModelForm
    success_url = reverse_lazy("nippo-list")
    def get_form_kwargs(self):
        kwgs = super().get_form_kwargs()
        print(kwgs)
        print(self.request)
        kwgs["user"] = self.request.user
        print(kwgs )
        return kwgs
    def form_valid(self, form):
        data = form.cleaned_data
        data["user"] = self.request.user
        obj = NippoModel(**data)
        print(self.request.user,"form_valid-------")
        print(form.cleaned_data,"form_valid-------")
        #print(NippoModel(**data))
        obj.save()
        return super().form_valid(form)



class NippoUpdateFormView(OwnerOnly,UpdateView):
    template_name = "nippo/nippo-formclass.html"
    model = NippoModel
    form_class = NippoModelForm
    success_url = reverse_lazy("nippo-list")

class NippoDeleteView(OwnerOnly,DeleteView):
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