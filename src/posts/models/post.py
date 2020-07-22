from datetime import datetime
from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify

from accounts.models import Member
from campaigns.models import Campaign

class Post(models.Model):
    slug = models.SlugField(max_length=180, unique=True, blank=True)
    title = models.CharField(max_length=150, blank=True)
    content = models.TextField(blank=True)
    author = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='posts', blank=True)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='posts', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        today = datetime.today()
        title_slugified = slugify(self.title)
        self.slug = f'{today:%Y%m%d%M%S%f}-{title_slugified}'
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

    def post_reply_url(self):
        return reverse("post-api:replies", kwargs={"slug": self.slug})

    def get_replies(self):
        return self.replies.filter(post=self).order_by('-created_at')

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'