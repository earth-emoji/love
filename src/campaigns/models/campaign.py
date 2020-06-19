from datetime import datetime
from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify

from accounts.models import Member
from campaigns.models import Cause

class Campaign(models.Model):
    slug = models.SlugField(max_length=128, unique=True, blank=True)
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(null=True, blank=True)
    funds_needed = models.DecimalField(max_digits=11, decimal_places=2, null=True, blank=True)
    funds_raised = models.DecimalField(max_digits=11, decimal_places=2, null=True, blank=True)
    funds_available = models.DecimalField(max_digits=11, decimal_places=2, null=True, blank=True)
    is_open = models.BooleanField(default=True, blank=True)
    is_active = models.BooleanField(default=True, blank=True)
    closing_statement = models.TextField(null=True, blank=True)
    volunteers_needed = models.PositiveIntegerField(default=0, blank=True)
    volunteers = models.ManyToManyField(Member, related_name='volunteer_work', through='Volunteer')
    initiator = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="campaigns", blank=True)
    cause = models.ForeignKey(Cause, on_delete=models.CASCADE, related_name="campaigns", blank=True)

    @property
    def volunteer_url(self):
        return "/campaigns/%s/volunteer/" % (self.slug)

    def get_absolute_url(self):
        return reverse("campaigns:details", kwargs={"slug": self.slug})

    def get_conversations(self):
        return self.topic.conversations.all()

    def get_volunteers(self):
        return self.volunteers.filter(status="Accepted")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        today = datetime.today()
        title_slugified = slugify(self.title)
        self.slug = f'{today:%Y%m%d%M%S%f}-{title_slugified}'
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'campaign'
        verbose_name_plural = 'campaigns'