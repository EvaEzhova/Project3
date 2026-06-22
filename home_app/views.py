from django.shortcuts import render
from django.views.generic import CreateView, ListView
from .models import Post
from django.urls import reverse_lazy
# Create your views here.
class PostView(ListView):
    template_name = 'home_app/posts.html'
    model = Post
    context_object_name = 'posts'


class PostCreateView(CreateView):
    model = Post
    template_name = 'home_app/create.html'
    fields = ["name", "image"]
    success_url = reverse_lazy("post")
