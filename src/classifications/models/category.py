import uuid
from django.db import models

# from classifications.choices import CONTENT_TYPE_CHOICES

class Category(models.Model):
    slug = models.SlugField(unique=True, default=uuid.uuid1, blank=True)
    name = models.CharField(max_length=60, unique=True, blank=True)
    # content_type = models.CharField(max_length=10, choices=CONTENT_TYPE_CHOICES, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'