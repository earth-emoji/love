from datetime import datetime
from django.db import models

from accounts.models import Member
from contacts.models import ContactGroup

class Message(models.Model):
    group = models.ForeignKey(ContactGroup, on_delete=models.CASCADE, related_name="messages", blank=True)
    author = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="messages", blank=True)
    text = models.TextField(default="")
    date_created = models.DateTimeField(default=datetime.now)