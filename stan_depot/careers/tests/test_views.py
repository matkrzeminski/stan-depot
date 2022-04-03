import pytest
from django.core.exceptions import ValidationError
from django.urls import reverse
from pytest_django.asserts import assertContains
from .factories import job_offer, generate_pdf, generate_doc, generate_docx

# from ..utils.generate_files import generate_pdf
from ..views import JobOfferListView, JobOfferDetailView, JobOfferThankYouView

pytestmark = pytest.mark.django_db


def test_job_offer_list_view(rf):
    url = reverse("careers:list")
    request = rf.get(url)
    response = JobOfferListView.as_view()(request)
    assertContains(response, "Job listings")


def test_job_offer_detail_view(rf, job_offer):
    url = reverse("careers:detail", kwargs={"slug": job_offer.slug})
    request = rf.get(url)
    response = JobOfferDetailView.as_view()(request, slug=job_offer.slug)
    assertContains(response, job_offer.description)


def test_job_offer_thank_you_view(rf):
    url = reverse("careers:thanks")
    request = rf.get(url)
    response = JobOfferThankYouView.as_view()(request)
    assertContains(response, "Thank You")


def test_job_offer_detail_form_pdf(rf, generate_pdf, job_offer):
    with open(generate_pdf, "rb") as file:
        form_data = {"email": "test@test.com", "first_name": "Test", "resume": file}
        url = reverse("careers:detail", kwargs={"slug": job_offer.slug})
        request = rf.post(url, data=form_data)
        callable_obj = JobOfferDetailView.as_view()
        response = callable_obj(request, slug=job_offer.slug)
        assert response.status_code == 302
        assert response.url == "/careers/thank-you/"


def test_job_offer_detail_form_doc(rf, generate_doc, job_offer):
    with open(generate_doc, "rb") as file:
        form_data = {"email": "test@test.com", "first_name": "Test", "resume": file}
        url = reverse("careers:detail", kwargs={"slug": job_offer.slug})
        request = rf.post(url, data=form_data)
        callable_obj = JobOfferDetailView.as_view()
        response = callable_obj(request, slug=job_offer.slug)
        assert response.status_code == 302
        assert response.url == "/careers/thank-you/"


def test_job_offer_detail_form_docx(rf, generate_docx, job_offer):
    with open(generate_docx, "rb") as file:
        form_data = {"email": "test@test.com", "first_name": "Test", "resume": file}
        url = reverse("careers:detail", kwargs={"slug": job_offer.slug})
        request = rf.post(url, data=form_data)
        callable_obj = JobOfferDetailView.as_view()
        response = callable_obj(request, slug=job_offer.slug)
        assert response.status_code == 302
        assert response.url == "/careers/thank-you/"


def test_job_offer_detail_form_invalid(rf, job_offer):
    form_data = {"email": "test@test.com", "resume": "test.png"}
    url = reverse("careers:detail", kwargs={"slug": job_offer.slug})
    request = rf.post(url, data=form_data)
    response = JobOfferDetailView.as_view()(request, slug=job_offer.slug)
    assert response.status_code == 200
    assert response.template_name[0] == "careers/detail.html"


def test_job_offer_detail_form_invalid_content_type(rf, generate_pdf, job_offer):
    with open(generate_pdf, "rb") as file:
        file.content_type = "image/png"
        form_data = {"email": "test@test.com", "first_name": "Test", "resume": file}
        url = reverse("careers:detail", kwargs={"slug": job_offer.slug})
        request = rf.post(url, data=form_data)
        with pytest.raises(ValidationError) as err:
            response = JobOfferDetailView.as_view()(request, slug=job_offer.slug)
            err.match("Content type not supported.")
            assert response.status_code == 200
            assert response.template_name[0] == "careers/detail.html"
