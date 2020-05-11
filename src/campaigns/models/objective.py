import uuid
from django.db import models

from campaigns.models import Goal

class Objective(models.Model):
    slug = models.SlugField(unique=True, default=uuid.uuid1, blank=True)
    short_desc = models.CharField(max_length=100, blank=True)
    long_desc = models.TextField(blank=True)
    percent_complete = models.FloatField(default=0.0, blank=True)
    is_complete = models.BooleanField(default=False, blank=True)
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, related_name="objectives", blank=True)

    def __str__(self):
        return self.short_desc

    class Meta:
        verbose_name = 'objective'
        verbose_name_plural = 'objectives'
