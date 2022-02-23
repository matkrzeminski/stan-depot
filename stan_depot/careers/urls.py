from django.urls import path

from . import views

app_name = "careers"

urlpatterns = [
    path("", views.JobOfferListView.as_view(), name="list"),
    path("thank-you/", views.JobOfferThankYouView.as_view(), name="thanks"),
    path("<slug:slug>", views.JobOfferDetailView.as_view(), name="detail"),
]
