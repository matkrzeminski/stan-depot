import pytest
from markdownx.utils import markdownify

from .factories import post


pytestmark = pytest.mark.django_db


def test__str__(post):
    assert post.__str__() == post.title
    assert str(post) == post.title


def test_get_absolute_url(post):
    url = post.get_absolute_url()
    assert url == f'/blog/{post.slug}/'


def test_formatted_content(post):
    assert post.formatted_content == markdownify(post.content)
