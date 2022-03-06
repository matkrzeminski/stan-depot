import factory
import factory.fuzzy
import pytest
from django.core.files.base import ContentFile
from slugify import slugify

from ..models import Post


class PostFactory(factory.django.DjangoModelFactory):
    title = factory.fuzzy.FuzzyText()
    hero = factory.LazyAttribute(
        lambda _: ContentFile(factory.django.ImageField()
                              ._make_data({'width': 3840, 'height': 2160}),
                              'test.jpg'))
    slug = factory.LazyAttribute(lambda obj: slugify(obj.title))
    content = factory.Faker("paragraph", nb_sentences=350, variable_nb_sentences=True)
    status = factory.fuzzy.FuzzyChoice(x[0] for x in Post.Status.choices)

    class Meta:
        model = Post


@pytest.fixture
def post():
    return PostFactory()
