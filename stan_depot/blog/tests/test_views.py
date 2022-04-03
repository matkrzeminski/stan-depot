import pytest
from django.urls import reverse
from pytest_django.asserts import assertContains
from ..tests.factories import post
from ..views import BlogHomeListView, BlogPostDetailView, PostListAPIView

pytestmark = pytest.mark.django_db


def test_blog_home_list_view(rf):
    url = reverse("blog:list")
    request = rf.get(url)
    response = BlogHomeListView.as_view()(request)
    assertContains(response, "Blog")
    assert response.status_code == 200
    assert response.template_name[0] == "blog/list.html"


def test_blog_post_detail_view(rf, post):
    url = reverse("blog:post", kwargs={"slug": post.slug})
    request = rf.get(url)
    response = BlogPostDetailView.as_view()(request, slug=post.slug)
    assertContains(response, post.title)
    assertContains(response, post.hero)
    assertContains(response, post.formatted_content)
    assert response.status_code == 200
    assert response.template_name[0] == "blog/detail.html"
