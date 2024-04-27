from django.db import models
import uuid
from django.utils import timezone


class AbstractBaseModel(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)

    class Meta:
        abstract = True