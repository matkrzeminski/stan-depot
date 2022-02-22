import pytest

from .factories import place
from ..utils.process_geocoder_data import process_geocoder_data

pytestmark = pytest.mark.django_db


def test__str__(place):
    assert place.__str__() == f"{place.name} {place.address}"
    assert str(place) == f"{place.name} {place.address}"


def test_get_absolute_url(place):
    url = place.get_absolute_url()
    assert url == "/contact/"


def test_save(place):
    import geocoder
    g = geocoder.osm(place.address)
    data = process_geocoder_data(g)
    if data:
        assert place.latitude == data.get("latitude")
        assert place.longitude == data.get("longitude")
        assert place.street == data.get("street")
        assert place.city == data.get("city")
        assert place.zip_code == data.get("zip_code")
        assert place.country == data.get("country")
    else:
        assert place.latitude == ""
        assert place.longitude == ""
        assert place.street == ""
        assert place.city == ""
        assert place.zip_code == ""
        assert place.country == ""
