from django.views.generic import ListView, DetailView

from .models import Post


class BlogHomeListView(ListView):
    model = Post
    template_name = 'blog/list.html'


class BlogPostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
