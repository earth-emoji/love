from datetime import datetime
from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify

from accounts.models import Member
from campaigns.models import Campaign
from discussions.models import Discussion

class Topic(models.Model):
    slug = models.SlugField(max_length=128, unique=True, blank=True)
    name = models.CharField(max_length=100, unique=True, blank=True)
    description = models.TextField(blank=True)
    campaign = models.OneToOneField(Campaign, on_delete=models.CASCADE, null=True, blank=True)
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE, related_name='topics', null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("topics:details", kwargs={"slug": self.slug})

    def new_conversations_url(self):
        return reverse("topics:new-conversation", kwargs={"slug": self.slug})

    def get_conversations(self):
        return self.conversations.filter(topic=self)

    def save(self, *args, **kwargs):
        today = datetime.today()
        title_slugified = slugify(self.name)
        self.slug = f'{today:%Y%m%d%M%S}-{title_slugified}'
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'topic'
        verbose_name_plural = 'topics'