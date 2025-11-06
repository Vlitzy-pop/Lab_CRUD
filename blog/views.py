from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin

class BlogListView(LoginRequiredMixin , ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    login_url = 'login'

class BlogDetailView(LoginRequiredMixin , DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    login_url = 'login'
    
# Create your views here.
