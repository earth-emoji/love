import uuid
from django.db import models

from campaigns.models import Campaign

class Goal(models.Model):
    slug = models.SlugField(unique=True, default=uuid.uuid1, blank=True)
    short_desc = models.CharField(max_length=100, blank=True)
    long_desc = models.TextField(blank=True)
    percent_complete = models.FloatField(default=0.0, blank=True)
    is_complete = models.BooleanField(default=False, blank=True)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name="goals", blank=True)

    def __str__(self):
        return self.short_desc

    class Meta:
        verbose_name = 'goal'
        verbose_name_plural = 'goals'
