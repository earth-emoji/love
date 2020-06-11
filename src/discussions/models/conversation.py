from datetime import datetime
from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify

from accounts.models import Member
from campaigns.models import Campaign
from discussions.models import Topic

class Conversation(models.Model):
    slug = models.SlugField(max_length=80, unique=True, blank=True)
    title = models.CharField(max_length=50, blank=True)
    content = models.TextField(blank=True)
    is_private = models.BooleanField(default=False, blank=True)
    allowed_members = models.ManyToManyField(Member, related_name='private_conversations', blank=True)
    blacklist = models.ManyToManyField(Member, related_name='blacklisted_conversations', blank=True)
    author = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='conversations', blank=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='conversations', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author.user.email

    def save(self, *args, **kwargs):
        today = datetime.today()
        title_slugified = slugify(self.title)
        self.slug = f'{today:%Y%m%d%M%S}-{title_slugified}'
        super().save(*args, **kwargs)

    @property
    def timelapse(self):
        time = datetime.now()
        if self.created_at.hour == time.hour:
            return str(time.minute - self.created_at.minute) + " minutes ago"
        else:
            if self.created_at.day == time.day:
                return str(time.hour - self.created_at.hour) + " hours ago"
            else:
                if self.created_at.month == time.month:
                    return str(time.day - self.created_at.day) + " days ago"
                else:
                    if self.created_at.year == time.year:
                        return str(time.month - self.created_at.month) + " months ago"
        return self.created_at

    def conversation_reply_url(self):
        return reverse("conversations-api:replies", kwargs={"slug": self.slug})

    def get_replies(self):
        return self.replies.filter(conversation=self).order_by('-created_at')

    class Meta:
        verbose_name = 'conversation'
        verbose_name_plural = 'conversations'