import uuid
from django.db import models

from accounts.models import Member

from events.models import Event

class Invitation(models.Model):
    slug = models.SlugField(unique=True, default=uuid.uuid1, blank=True)
    attendee = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='invitations', blank=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='invitations', blank=True)
    accepted = models.BooleanField(default=False, blank=True)
    published_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'invitation'
        verbose_name_plural = 'invitations'