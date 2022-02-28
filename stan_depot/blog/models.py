import os
from io import BytesIO

from PIL import Image
from autoslug import AutoSlugField
from django.core.files.base import ContentFile
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

    title = models.CharField("Title", max_length=120)
    hero = models.ImageField("Hero", upload_to="blog/heroes", blank=True)
    thumbnail = models.ImageField(upload_to="blog/thumbs", blank=True, editable=False)
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

    def save(self, *args, **kwargs):
        if not self.hero:
            super().save(*args, **kwargs)
            return
        if not self.make_thumbnail():
            raise Exception("Could not create thumbnail")
        super().save(*args, **kwargs)

    def make_thumbnail(self):
        """Generates 200x200 thumbnail from the given hero image.
         Accepts .jpg, .jpeg, .gif, .png."""
        image = Image.open(self.hero)
        image.thumbnail((200, 200))

        thumb_name, thumb_extension = os.path.splitext(self.hero.name)
        thumb_extension = thumb_extension.lower()

        thumb_filename = f"{thumb_name}_thumb{thumb_extension}"

        if thumb_extension in [".jpg", ".jpeg"]:
            FTYPE = "JPEG"
        elif thumb_extension == ".gif":
            FTYPE = "GIF"
        elif thumb_extension == ".png":
            FTYPE = "PNG"
        else:
            return False

        temp_thumb = BytesIO()
        image.save(temp_thumb, FTYPE)
        temp_thumb.seek(0)

        self.thumbnail.save(thumb_filename, ContentFile(temp_thumb.read()), save=False)
        temp_thumb.close()

        return True

    def formatted_markdown(self):
        return markdownify(self.content)
