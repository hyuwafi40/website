from django.db import models
from solo.models import SingletonModel


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True


class BaseSingletonModel(TimeStampedModel, SingletonModel):
    class Meta:
        abstract = True

    def __str__(self):
        return self.name
