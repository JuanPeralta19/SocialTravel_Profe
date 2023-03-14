from django.shortcuts import render
from SocialTravel.models import post
from SocialTravel.forms import postForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

def index(request):
    return render(request, "SocialTravel/index.html")


def mostrar_posts(request):
    context = {
         "posts": post.objects.all(),
         "form": postForm(),
         }

    
    return render(request, "SocialTravel/admin_post.html", context)


def agregar_post(request):
    post_form = postForm(request.POST)
    post_form.save()
    context = {
         "posts": post.objects.all(),
         "form": postForm(),
         }

    return render(request, "SocialTravel/admin_post.html", context)


def buscar_post(request):
    criterio = request.GET.get("criterio")
    context = { "posts": post.objects.filter(carousel_caption_title__icontains=criterio).all()}
    return render(request, "SocialTravel/admin_post.html", context)

class PostList(ListView):
    model = post
