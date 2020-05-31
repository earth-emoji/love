import uuid
from django.db import models

# from classifications.choices import CONTENT_TYPE_CHOICES

class Tag(models.Model):
    slug = models.SlugField(unique=True, default=uuid.uuid1, blank=True)
    name = models.CharField(max_length=60, unique=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'