from datetime import datetime
from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify

from accounts.models import Member
from campaigns.models import Campaign

class Team(models.Model):
    slug = models.SlugField(max_length=80, unique=True, blank=True)
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

    def save(self, *args, **kwargs):
        today = datetime.today()
        title_slugified = slugify(self.name)
        self.slug = f'{today:%Y%m%d%M%S}-{title_slugified}'
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'team'
        verbose_name_plural = 'teams'
