from datetime import datetime
from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify

from accounts.models import Member
from classifications.models import Tag
from discussions.models import Discussion

class Topic(models.Model):
    slug = models.SlugField(max_length=80, unique=True, blank=True)
    name = models.CharField(max_length=60, blank=True)
    description = models.TextField(blank=True)
    tags = models.ManyToManyField(Tag, related_name='topics', blank=True)
    moderator = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='topics', blank=True)
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE, related_name='topics', blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("topics:thread", kwargs={"slug": self.slug})

    def new_entry_url(self):
        return reverse("topics-api:entries", kwargs={"slug": self.slug})

    def get_entries(self):
        return self.entries.filter(topic=self)

    def save(self, *args, **kwargs):
        today = datetime.today()
        title_slugified = slugify(self.name)
        self.slug = f'{today:%Y%m%d%M%S}-{title_slugified}'
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'topic'
        verbose_name_plural = 'topics'