import uuid
from django.db import models
from django.shortcuts import reverse
from accounts.models import Member
from discussions.models import Conversation

class Reply(models.Model):
    slug = models.SlugField(unique=True, default=uuid.uuid1, blank=True)
    content = models.TextField(blank=True)
    author = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='replies', blank=True)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='replies', blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='replies', null=True, blank=True)
    is_published = models.BooleanField(default=True, blank=True)
    published_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # def get_absolute_url(self):
    #     return reverse("model_detail", kwargs={"pk": self.pk})
    @property
    def conversation_reply_url(self):
        return reverse("replies-api:reply", kwargs={"slug": self.slug})

    def get_replies(self):
        """Return replies of a comment."""
        return Reply.objects.filter(parent=self).order_by('-created_at')

    def __str__(self):
        return f"{self.author.get_name} replies to {self.conversation.title}"

    class Meta:
        verbose_name = 'reply'
        verbose_name_plural = 'replies'
