from django.urls import reverse, resolve


def test_contact_reverse():
    """contact:home should reverse to /contact/."""
    assert reverse("contact:home") == "/contact/"


def test_contact_resolve():
    """/contact/ should resolve to contact:home."""
    assert resolve("/contact/").view_name == "contact:home"


def test_thanks_reverse():
    """contact:thanks should reverse to /contact/thank-you/"""
    assert reverse("contact:thanks") == "/contact/thank-you/"


def test_thanks_resolve():
    """/contact/thank-you/ should resolve to contact:thanks."""
    assert resolve("/contact/thank-you/").view_name == "contact:thanks"


def test_place_list_reverse():
    """contact:place-list should reverse to /contact/api/places/."""
    assert reverse("contact:place-list") == "/contact/api/places/"


def test_place_list_resolve():
    """/contact/api/places/ should resolve to contact:place-list."""
    assert resolve("/contact/api/places/").view_name == "contact:place-list"
