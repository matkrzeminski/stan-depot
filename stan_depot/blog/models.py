from autoslug import AutoSlugField
from django.db import models
from django.urls import reverse
from django.utils import timezone
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
from model_utils.models import TimeStampedModel


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status="published")


class Post(TimeStampedModel):
    class Status(models.TextChoices):
        PUBLISHED = "published", "Published"
        DRAFT = "draft", "Draft"

    title = models.CharField(("Title"), max_length=120)
    hero = models.ImageField("Hero", upload_to="blog/heroes", blank=True)
    slug = AutoSlugField(
        "Post address", unique=True, always_update=False, populate_from="title"
    )
    content = MarkdownxField("Content", blank=True)
    status = models.CharField("Status", max_length=9, choices=Status.choices, default=Status.DRAFT)
    publish = models.DateTimeField(default=timezone.now)
    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ("-publish",)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:post", kwargs={"slug": self.slug})

    @property
    def formatted_content(self):
        return markdownify(self.content)
