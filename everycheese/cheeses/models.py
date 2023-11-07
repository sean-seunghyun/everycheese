from django.db import models

from autoslug import AutoSlugField
from model_utils.models import TimeStampedModel


class Cheese(TimeStampedModel):

    class Firmness(models.TextChoices):
        UNSPECIFED = "unspecifed", "Unspecifed"
        SOFT = "soft", "Soft"
        SEMI_SOFT = "semi-soft", "Semi-soft"
        SEMI_HARD = "semi-hard", "Semi-hard"
        HARD = "hard", "Hard"

    name = models.CharField("Name of Cheese", max_length=255)
    slug = AutoSlugField("Cheese Address", unique=True, always_update=False, populate_from="name")
    description = models.TextField("Description", blank=True)
    firmness = models.CharField("Frimness", max_length=20, choices=Firmness.choices, default=Firmness.UNSPECIFED)

    def __str__(self):
        return self.name

