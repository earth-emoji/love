from datetime import datetime
import uuid
from django.db import models
from django.shortcuts import reverse

from accounts.models import Member
from campaigns.models import Campaign

class Post(models.Model):
    slug = models.SlugField(unique=True, default=uuid.uuid1, blank=True)
    title = models.CharField(max_length=30, blank=True)
    content = models.TextField(blank=True)
    author = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='posts', blank=True)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='posts', blank=True)
    is_published = models.BooleanField(default=False, blank=True)
    published_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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

    def get_absolute_url(self):
        return reverse("posts:details", kwargs={"slug": self.slug})

    @property
    def post_comment_url(self):
        return reverse("posts-api:comment", kwargs={"slug": self.slug})

    def get_comments(self):
        return self.comments.filter(post=self).order_by('-created_at')

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
