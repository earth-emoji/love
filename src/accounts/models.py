import uuid

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from . import choices


class MemberManager(models.Manager):
    use_for_related_fields = True


class Member(models.Model):
    slug = models.SlugField(unique=True, default=uuid.uuid1, blank=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name="member", on_delete=models.CASCADE, blank=True)
    
    objects = MemberManager()

    class Meta:
        verbose_name = _('member')
        verbose_name_plural = _('members')

    def __str__(self):
        return self.user.username

