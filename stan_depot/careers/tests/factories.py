import factory
import factory.fuzzy
import pytest
from django.template.defaultfilters import slugify

from stan_depot.careers.models import JobOffer
from stan_depot.contact.tests.factories import PlaceFactory


class JobOfferFactory(factory.django.DjangoModelFactory):
    title = factory.fuzzy.FuzzyText()
    slug = factory.LazyAttribute(lambda obj: slugify(obj.title))
    description = factory.Faker("paragraph", nb_sentences=5, variable_nb_sentences=True)
    location = factory.SubFactory(PlaceFactory)
    compensation_min = factory.fuzzy.FuzzyInteger(5000, 10000)
    compensation_max = factory.fuzzy.FuzzyInteger(15000, 25000)
    status = factory.fuzzy.FuzzyChoice(x[0] for x in JobOffer.Status.choices)

    class Meta:
        model = JobOffer


@pytest.fixture
def job_offer():
    return JobOfferFactory()
