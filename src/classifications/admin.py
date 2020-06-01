from django.contrib import admin

from classifications.models import Category, Tag, Cause

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Cause)
