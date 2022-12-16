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
from django.core.mail import send_mail
from django.template.loader import render_to_string


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
    
def reqest_mail(request,pk):
    template_name = "nippo/send_mail.html"
    subject = "試合の申請"
    ctx={}
    qs = NippoModel.objects.get(pk=pk)
    print("print",qs,"~~~~~~~~~~~~~~~~~~~~~~")
    qs2 = NippoModel.objects.all()
    print("print",qs2,"~~~~~~~~~~~~~~~~~~~~~~")
    ctx["login_user"]= str(request.user) #ログインユーザーを取得する
    ctx["user"]= str(qs.user)
    ctx["date"]= str(qs.date)
    '''
    ctx["login_user_str"]= str(ctx["login_user"].copy()) #ログインユーザーを取得する
    ctx["user_str"]= str(ctx["user"].copy())
    ctx["date_str"]= str(ctx["date"].copy())
    print("print",ctx["login_user_str"],"~~~~~~~~~~~~~~~~~~~~~~")
    print("print",ctx["user_str"],"~~~~~~~~~~~~~~~~~~~~~~")
    print("print",ctx["date_str"],"~~~~~~~~~~~~~~~~~~~~~~")
    '''
    from_email = request.user # 送信者
    recipient_list = [
        ctx["user"]
    ]
    
    message = render_to_string("mailers/reqest_mail.txt",ctx)
    send_mail(subject, message, from_email, recipient_list)
    return render(request, template_name,ctx)  

    
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