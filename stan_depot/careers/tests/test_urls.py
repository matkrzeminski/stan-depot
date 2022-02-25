import pytest
from django.urls import reverse, resolve
from .factories import job_offer


pytestmark = pytest.mark.django_db


def test_job_offer_reverse():
    """careers:list should reverse to /careers/."""
    assert reverse("careers:list") == "/careers/"


def test_job_offer_resolve():
    """/careers/ should resolve to careers:list."""
    assert resolve("/careers/").view_name == "careers:list"


def test_thanks_reverse():
    """careers:thanks should reverse to /careers/thank-you/"""
    assert reverse("careers:thanks") == "/careers/thank-you/"


def test_thanks_resolve():
    """/careers/thank-you/ should resolve to careers:thanks."""
    assert resolve("/careers/thank-you/").view_name == "careers:thanks"


def test_job_offer_detail_reverse(job_offer):
    """careers:place-list should reverse to /careers/<slug:slug>/."""
    url = reverse("careers:detail", kwargs={"slug": job_offer.slug})
    assert url == f"/careers/{job_offer.slug}/"


def test_job_offer_detail_resolve(job_offer):
    """/careers/<slug:slug>/ should resolve to careers:detail."""
    url = f"/careers/{job_offer.slug}/"
    assert resolve(url).view_name == "careers:detail"
