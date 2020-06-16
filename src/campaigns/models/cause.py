from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify

from accounts.models import Member
from campaigns.choices import CAUSE_CATEGORY_CHOICES

class Cause(models.Model):
    slug = models.SlugField(max_length=80, unique=True, blank=True)
    name = models.CharField(max_length=60, unique=True, blank=True)
    category = models.CharField(max_length=15, choices=CAUSE_CATEGORY_CHOICES, blank=True)
    supporters = models.ManyToManyField(Member, related_name='causes', blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'cause'
        verbose_name_plural = 'causes'