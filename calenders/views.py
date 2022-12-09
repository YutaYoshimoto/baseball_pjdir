from django.shortcuts import render,get_object_or_404,redirect
from random import randint
from .models import NippoModel
from .forms import  NippoFormClass,ImageUploadForm#,NippoModelForm
from django.views.generic.edit import CreateView
from django.views.generic import ListView,DetailView,FormView,DeleteView
from django.urls import reverse, reverse_lazy



class NippoDetailView(DetailView):
    template_name = "nippo/nippo-detail.html"
    #model = NippoModel #1
    def get_queryset(self):
        return  NippoModel.objects.all()
#上記クラスに変更
def nippoDetailView(request, pk):
     template_name = "nippo/nippo-detail.html"
     ctx = {}
     q = get_object_or_404(NippoModel, pk=pk)
     ctx["object"] = q
     return render(request, template_name, ctx)

   
                         
class NippoListView(ListView):
    template_name = "nippo/nippo-list.html"
 #model = NippoModel #1
    def get_queryset(self):
        return  NippoModel.objects.all()
#上記クラスに変更
def nippoListView(request):
    template_name = "nippo/nippo-list.html"
    ctx = {}
    qs = NippoModel.objects.all()
    ctx["object_list"] = qs
    return render(request, template_name, ctx)


def nippoCreateFormView(request):
    template_name = "nippo/nippo-formclass.html"
    form = NippoFormClass(request.POST or None)
    ctx = {"form": form}
    if form.is_valid():
        title = form.cleaned_data["title"]
        content = form.cleaned_data["content"]
        obj = NippoModel(title=title, content=content)
        obj.save()
        return redirect("nippo-list")
    return render(request, template_name, ctx)

class NippoCreateFormView(FormView):
    template_name = "nippo/nippo-formclass.html"
    form_class = NippoFormClass
    success_url = reverse_lazy("nippo-list")

    def form_valid(self, form):
        data = form.cleaned_data
        obj = NippoModel(**data)
        obj.save()
        return super().form_valid(form)
#上記クラスに変更
def nippoCreateView(request):
    template_name = "nippo/nippo-form.html"
    form = NippoFormClass(request.POST or None)
    ctx = {"form": form}
    if form.is_valid():
        title = form.cleaned_data["title"]
        content = form.cleaned_data["content"]
        obj = NippoModel(title=title, content=content)
        obj.save()
    return render(request, template_name, ctx)


def nippoUpdateFormView(request, pk):
    template_name = "nippo/nippo-formclass.html"
    obj = get_object_or_404(NippoModel, pk=pk)
    initial_values = {"title": obj.title, "content":obj.content}
    form = NippoFormClass(request.POST or initial_values)
    ctx = {"form": form}
    ctx["object"] = obj
    if form.is_valid():
        title = form.cleaned_data["title"]
        content = form.cleaned_data["content"]
        obj.title = title
        obj.content = content
        obj.save()
        if request.POST:
            return redirect("nippo-list")
    return render(request, template_name, ctx)

class NippoDeleteView(DeleteView):
    template_name = "nippo/nippo-delete.html"
    model = NippoModel
    success_url = reverse_lazy("nippo-list")
#上記クラスに変更    
def nippoDeleteView(request, pk):
    template_name = "nippo/nippo-delete.html"
    obj = get_object_or_404(NippoModel, pk=pk)
    ctx = {"object": obj}
    if request.POST:
        obj.delete()
        return redirect("nippo-list")
    return render(request, template_name, ctx)



class ImageUploadView(CreateView):
    template_name = "nippo/image-upload.html"
    form_class = ImageUploadForm
    success_url = "/"
    
'''
class NippoCreateFormView(CreateView):
    template_name = "nippo/nippo-formclass.html"
    form_class = NippoModelForm
    success_url = reverse_lazy("nippo-list")
'''