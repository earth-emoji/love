import uuid
from datetime import datetime
from django.db import models
from django.shortcuts import reverse

from accounts.models import Member
from discussions.models import Topic

class Entry(models.Model):
    slug = models.SlugField(unique=True, default=uuid.uuid1, blank=True)
    content = models.TextField(blank=True)
    author = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='entries', blank=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='entries', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author.user.email

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

    def entry_reply_url(self):
        return reverse("entries-api:replies", kwargs={"slug": self.slug})

    def get_replies(self):
        return self.replies.filter(entry=self).order_by('-created_at')

    class Meta:
        verbose_name = 'entry'
        verbose_name_plural = 'entries'