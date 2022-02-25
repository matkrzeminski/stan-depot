import pytest
from django.urls import reverse
from pytest_django.asserts import assertContains
from ..tests.factories import place
from ..views import ContactPageView, ThankYouPageView, PlaceListAPIView

pytestmark = pytest.mark.django_db


def test_contact_get_view(rf):
    url = reverse("contact:home")
    request = rf.get(url)
    response = ContactPageView.as_view()(request)
    assertContains(response, "Contact")


def test_contact_form_valid(rf):
    form_data = {
        "email": "test@test.com",
        "subject": "Test subject",
        "message": "Test message"
    }
    request = rf.post(reverse("contact:home"), form_data)
    response = ContactPageView.as_view()(request)
    assert response.status_code == 302
    assert response.url == "/contact/thank-you/"


def test_thanks_get_view(rf):
    url = reverse("contact:thanks")
    request = rf.get(url)
    response = ThankYouPageView.as_view()(request)
    assertContains(response, "Thank you")


def test_place_list_get_view(rf, place):
    url = reverse("contact:place-list")
    request = rf.get(url)
    response = PlaceListAPIView.as_view()(request)
    assertContains(response, str(place.street))
