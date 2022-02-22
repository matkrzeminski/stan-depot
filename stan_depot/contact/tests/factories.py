import factory.fuzzy
import pytest

from ..models import Place


class PlaceFactory(factory.django.DjangoModelFactory):
    name = factory.fuzzy.FuzzyText()
    address = factory.Faker("street_address", locale="pl_PL")

    class Meta:
        model = Place

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        address = kwargs.get("address")
        kwargs["address"] = address.replace("\n", " ")
        return super()._create(model_class, *args, **kwargs)


@pytest.fixture
def place():
    return PlaceFactory()
