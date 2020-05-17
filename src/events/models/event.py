import uuid
from django.db import models

from accounts.models import Member
from campaigns.models import Campaign

from events.choices import VISIBILITY_CHOICES

class Event(models.Model):
    slug = models.SlugField(unique=True, default=uuid.uuid1, blank=True)
    name = models.CharField(max_length=255, blank=True)
    description = models.TextField(default='', blank=True)
    start_time = models.DateTimeField(blank=True)
    end_time = models.DateTimeField(blank=True)
    visibility = models.CharField(max_length=9, choices=VISIBILITY_CHOICES, blank=True)
    is_published = models.BooleanField(default=False)
    published_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='events', blank=True)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='events', blank=True)
    attendees = models.ManyToManyField(Member, related_name='events_attended', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'event'
        verbose_name_plural = 'events'