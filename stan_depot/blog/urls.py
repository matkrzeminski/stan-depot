from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path("", views.BlogHomeListView.as_view(), name="list"),
    path("<slug:slug>/", views.BlogPostDetailView.as_view(), name="post")
]
