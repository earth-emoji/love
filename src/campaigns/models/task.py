import uuid
from django.db import models

from accounts.models import Member

from campaigns.models import Strategy

class Task(models.Model):
    slug = models.SlugField(unique=True, default=uuid.uuid1, blank=True)
    short_desc = models.CharField(max_length=100, blank=True)
    long_desc = models.TextField(blank=True)
    percent_complete = models.FloatField(default=0.0, blank=True)
    is_complete = models.BooleanField(default=False, blank=True)
    strategy = models.ForeignKey(Strategy, on_delete=models.CASCADE, related_name="tasks", blank=True)
    assignees = models.ManyToManyField(Member, related_name='assignments')

    def __str__(self):
        return self.short_desc

    class Meta:
        verbose_name = 'task'
        verbose_name_plural = 'tasks'
