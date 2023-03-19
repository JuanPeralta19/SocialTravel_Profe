from django.shortcuts import render
from SocialTravel.models import post
from SocialTravel.forms import postForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
    return render(request, "SocialTravel/index.html")

class PostList(ListView):
    model = post
    context_object_name = "posts"

class PostDetail(DetailView):
    model = post
    context_object_name = "post"

class PostUpdate(LoginRequiredMixin, UpdateView):
    model = post
    success_url = reverse_lazy("post-list")
    fields = '__all__'

class PostDelete(LoginRequiredMixin, DeleteView):
    model = post
    context_object_name = "post"
    success_url = reverse_lazy("post-list")

class PostCreate(LoginRequiredMixin, CreateView):
    model = post
    context_object_name = "post"
    success_url = reverse_lazy("post-list")
    fields = "__all__"

class PostSearch(ListView):
    model = post
    context_object_name = "posts"
    def get_queryset(self):
        criterio = self.request.GET.get("criterio")
        result = post.objects.filter(carousel_caption_title__icontains=criterio).all()
        return result
    
class Login(LoginView):
    next_page = reverse_lazy("index")

class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = "Registration/signup.html"
    success_url = reverse_lazy("index")

class Logout(LogoutView):
    template_name = "Registration/logout.html"
    



    
    