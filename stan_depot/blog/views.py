from django.views.generic import ListView, DetailView
from rest_framework.generics import ListAPIView

from stan_depot.contact.utils import permissions
from .models import Post
from .serializers import PostSerializer
from .utils.pagination import PostPagination


class BlogHomeListView(ListView):
    model = Post
    template_name = "blog/list.html"


class BlogPostDetailView(DetailView):
    model = Post
    template_name = "blog/detail.html"


class PostListAPIView(ListAPIView):
    queryset = Post.published.all()
    serializer_class = PostSerializer
    pagination_class = PostPagination
    permission_classes = [permissions.ReadOnly]
