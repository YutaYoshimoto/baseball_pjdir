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
        """ This function is called when the form is instantiated. """
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user  # add the user to the form kwargs
        return kwargs
    
    def form_valid(self, form):
        """ This function is called when the form is submitted. Next call is save() """
        # variable form is an instance of NippoModelForm
        # call save() to save the form data to the database
        form.save()
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




class NippoReqestDetailView(DetailView):
    template_name = "nippo/nippo-reqest.html"
    def get_queryset(self):
        return  NippoModel.objects.all()   
    

    
def nipporeqestview(request):
    template_name = "nippo/nippo-reqest.html"
    ctx = {}
    qs = NippoModel.objects.all()
    ctx["object_user"] = qs      
    return render(request, template_name, ctx)

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