import uuid
from django.db import models

from accounts.models import Member

from campaigns.choices import REQUEST_STATUS_CHOICES
from campaigns.models import Campaign

class Volunteer(models.Model):
    slug = models.SlugField(unique=True, default=uuid.uuid1, blank=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE, blank=True)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, blank=True)
    reason = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=REQUEST_STATUS_CHOICES, blank=True)

    @property
    def response_url(self):
        return "/volunteers/%s/response/" % (self.slug)

    def __str__(self):
        return f"{self.member.get_name} for {self.campaign.title} ({self.status})"

    class Meta:
        verbose_name = 'volunteer'
        verbose_name_plural = 'volunteers'
