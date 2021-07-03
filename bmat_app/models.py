import uuid

from django.contrib.postgres.fields import ArrayField
from django.db import models


class MusicalWork(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=60, null=True)
    contributors = ArrayField(models.CharField(max_length=60))
    iswc = models.CharField(max_length=11, unique=True, blank=False, null=True)

    def __str__(self):
        return self.title
