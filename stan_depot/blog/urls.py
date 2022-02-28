from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path("", views.BlogHomeListView.as_view(), name="list"),
    path("api/posts/", views.PostListAPIView.as_view(), name="api"),
    path("<slug:slug>/", views.BlogPostDetailView.as_view(), name="post")
]
