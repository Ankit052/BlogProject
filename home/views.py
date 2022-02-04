from django.shortcuts import render
from django.contrib.auth.models import User
from django.views import View
from .models import Post
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView 
from django.views.generic.base import TemplateView

# Create your views here.
class IndexPageView(TemplateView):
    template_name = "index.html"


class UserDetailView(DetailView):
    model = User
    template_name = "author_detail.html"

class UserListView(ListView):
    model = User
    template_name = "author_list.html"
    paginate_by = 5


class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"

class PostListView(ListView):
    model = Post
    template_name = "Post_list.html"
    paginate_by = 5

    def get_queryset(self):
        queryset = Post.objects.all().order_by("-created_on")
        return queryset


        
    

