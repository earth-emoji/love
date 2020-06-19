import uuid
from datetime import datetime
from django.db import models

from accounts.models import Member
from contacts.models import ContactGroup

class Contact(models.Model):
    slug = models.SlugField(unique=True, default=uuid.uuid1, blank=True)
    group = models.ForeignKey(ContactGroup, on_delete=models.CASCADE, related_name="contacts", blank=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="connections", blank=True)
    details = models.CharField(max_length=255, default="", blank=True)
    is_volunteer = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"{self.member.get_username} in {self.group.title}"