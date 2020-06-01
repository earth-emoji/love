from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify

class Discussion(models.Model):
    slug = models.SlugField(max_length=80, unique=True, blank=True)
    name = models.CharField(max_length=60, unique=True, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("discussions:details", kwargs={"slug": self.slug})

    def post_topic_url(self):
        return reverse("discussions:new-topic", kwargs={"slug": self.slug})
    

    def get_topics(self):
        return self.topics.filter(discussion=self)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'discussion'
        verbose_name_plural = 'discussions'

