import uuid
from datetime import datetime

from django.db import models
from django.utils.text import slugify

from accounts.models import Member


class ContactGroup(models.Model):
    slug = models.SlugField(max_length=128, unique=True, blank=True)
    creator = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="contact_groups", blank=True)
    title = models.CharField(max_length=50)
    is_private = models.BooleanField(default=True)
    unique_code = models.SlugField(unique=True, default=uuid.uuid1, blank=True)
    date_created = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        today = datetime.today()
        title_slugified = slugify(self.title)
        self.slug = f'{today:%Y%m%d%M%S%f}-{title_slugified}'
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'contact group'
        verbose_name_plural = 'contact groups'
