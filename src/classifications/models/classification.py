from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify

# from classifications.choices import CONTENT_TYPE_CHOICES

class Classification(models.Model):
    slug = models.SlugField(max_length=80, unique=True, blank=True)
    name = models.CharField(max_length=60, unique=True, blank=True)
    # content_type = models.CharField(max_length=10, choices=CONTENT_TYPE_CHOICES, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'classification'
        verbose_name_plural = 'classifications'