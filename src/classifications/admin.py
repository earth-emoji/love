from django.contrib import admin

from classifications.models import Classification, Tag, Cause

@admin.register(Classification)
class ClassificationAdmin(admin.ModelAdmin):
    ordering = ['name']

@admin.register(Cause)
class CauseAdmin(admin.ModelAdmin):
    ordering = ['name']
    list_filter = ['classification']

admin.site.register(Tag)
