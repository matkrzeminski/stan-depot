from autoslug import AutoSlugField
from django.db import models
from markdownx.models import MarkdownxField

from model_utils.models import TimeStampedModel

from stan_depot.contact.models import Place


class JobOffer(TimeStampedModel):
    class Status(models.TextChoices):
        CLOSED = "closed", "Closed"
        ONGOING = "ongoing", "Ongoing"
        OPENING_SOON = "opening soon", "Opening Soon"

    title = models.CharField("Title for this position", max_length=255)
    slug = AutoSlugField(
        "Job offer address",
        unique_with=("title", "location"),
        always_update=False,
        populate_from="title",
    )
    description = MarkdownxField("Description", blank=True)
    location = models.ForeignKey(Place, on_delete=models.CASCADE)
    compensation_min = models.IntegerField("Min compensation")
    compensation_max = models.IntegerField("Max compensation")
    status = models.CharField(
        "Status", max_length=12, choices=Status.choices, default=Status.OPENING_SOON
    )

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return self.title
