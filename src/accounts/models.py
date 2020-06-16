from django.conf import settings
from django.db import models
from django.utils.text import slugify

from . import choices

class MemberManager(models.Manager):
    use_for_related_fields = True


class Member(models.Model):
    slug = models.SlugField(max_length=80, unique=True, blank=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name="member", on_delete=models.CASCADE, blank=True)

    objects = MemberManager()

    @property
    def get_username(self):
        return self.user.username

    @property
    def get_email(self):
        return self.user.email

    @property
    def get_avatar(self):
        return f"{settings.MEDIA_URL}{self.user.photo}"

    @property
    def get_name(self):
        return self.user.name

    @property
    def get_dob(self):
        return self.user.date_of_birth

    @property
    def get_sex(self):
        return self.user.sex

    @property
    def get_basket_count(self):
        return self.basket.items.count()

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'member'
        verbose_name_plural = 'members'