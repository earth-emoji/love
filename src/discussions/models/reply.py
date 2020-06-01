import uuid
from django.db import models
from django.shortcuts import reverse
from accounts.models import Member
from discussions.models import Entry

class Reply(models.Model):
    slug = models.SlugField(unique=True, default=uuid.uuid1, blank=True)
    content = models.TextField(blank=True)
    author = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='replies', blank=True)
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE, related_name='replies', blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='replies', null=True, blank=True)
    is_published = models.BooleanField(default=True, blank=True)
    published_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # def get_absolute_url(self):
    #     return reverse("model_detail", kwargs={"pk": self.pk})
    @property
    def entry_reply_url(self):
        return reverse("replies-api:reply", kwargs={"slug": self.slug})

    def get_replies(self):
        """Return replies of a comment."""
        return Reply.objects.filter(parent=self).order_by('-created_at')

    class Meta:
        verbose_name = 'reply'
        verbose_name_plural = 'replies'
