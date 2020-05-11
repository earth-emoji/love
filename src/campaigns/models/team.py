import uuid
from django.db import models

from accounts.models import Member
from campaigns.models import Campaign

class Team(models.Model):
    slug = models.SlugField(unique=True, default=uuid.uuid1, blank=True)
    name = models.CharField(max_length=60, blank=True)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='teams', blank=True)
    leader = models.ForeignKey(Member, on_delete=models.SET_NULL, related_name='teams_led', null=True, blank=True)
    members = models.ManyToManyField(Member, related_name="teams")

    @property
    def url(self):
        return "/teams/%s/" % (self.slug)

    @property
    def campaign_url(self):
        return "/campaigns/%s/teams/" % (self.campaign.slug)

    @property
    def campaign_json_url(self):
        return "/teams/campaigns/%s/" % (self.campaign.slug)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'team'
        verbose_name_plural = 'teams'
