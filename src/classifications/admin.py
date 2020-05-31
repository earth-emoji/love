from django.contrib import admin

from classifications.models import Category, Tag

admin.site.register(Category)
admin.site.register(Tag)