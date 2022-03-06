import pytest
from django.urls import reverse, resolve
from .factories import post


pytestmark = pytest.mark.django_db


def test_blog_home_reverse():
    """blog:list should reverse to /blog/."""
    assert reverse("blog:list") == "/blog/"


def test_blog_home_resolve():
    """/blog/ should resolve to blog:list."""
    assert resolve("/blog/").view_name == "blog:list"


def test_blog_post_detail_reverse(post):
    """blog:post should reverse to /blog/<slug:slug>/."""
    assert reverse("blog:post", kwargs={"slug": post.slug}) == f"/blog/{post.slug}/"


def test_blog_post_detail_resolve(post):
    """/blog/<slug:slug>/ should resolve to blog:post."""
    assert resolve(f"/blog/{post.slug}/").view_name == "blog:post"


def test_blog_post_api_reverse():
    """blog:api should reverse to /blog/api/posts/."""
    assert reverse("blog:api") == f"/blog/api/posts/"


def test_blog_post_api_resolve():
    """/blog/api/posts/ should resolve to blog:api."""
    assert resolve("/blog/api/posts/").view_name == "blog:api"
