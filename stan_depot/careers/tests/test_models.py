import pytest

from .factories import job_offer
from markdownx.utils import markdownify

pytestmark = pytest.mark.django_db


def test__str__(job_offer):
    assert job_offer.__str__() == job_offer.title
    assert str(job_offer) == job_offer.title


def test_get_absolute_url(job_offer):
    url = job_offer.get_absolute_url()
    assert url == f'/careers/{job_offer.slug}/'


def test_formatted_markdown(job_offer):
    assert job_offer.formatted_markdown() == markdownify(job_offer.description)
