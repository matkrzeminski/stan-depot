from django.urls import path

from . import views

app_name = "contact"

urlpatterns = [
    path("", views.ContactPageView.as_view(), name='home'),
    path("thanks/", views.ThankYouPageView.as_view(), name='thanks'),
    path("api/places/", views.PlaceListAPIView.as_view(), name='place-list'),
]
