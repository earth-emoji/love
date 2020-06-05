from datetime import datetime
from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify

from accounts.models import Member
from events.choices import VISIBILITY_CHOICES

class Event(models.Model):
    slug = models.SlugField(max_length=80, unique=True, blank=True)
    name = models.CharField(max_length=255, blank=True)
    details = models.TextField(default='', blank=True)
    location = models.CharField(max_length=200, blank=True)
    start_time = models.DateTimeField(blank=True)
    end_time = models.DateTimeField(blank=True)
    visibility = models.CharField(max_length=9, choices=VISIBILITY_CHOICES, blank=True)
    is_published = models.BooleanField(default=False)
    published_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='events', blank=True)
    attendees = models.ManyToManyField(Member, related_name='events_attended', blank=True)

    @property
    def get_listing_api(self):
        return reverse("events-api:listing")

    @property
    def formatted_start_time(self):
        return datetime.strftime(self.start_time, "%m-%d-%Y %I:%M %p")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        today = datetime.today()
        title_slugified = slugify(self.name)
        self.slug = f'{today:%Y%m%d%M%S}-{title_slugified}'
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'event'
        verbose_name_plural = 'events'