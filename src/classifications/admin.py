from django.contrib import admin

from classifications.models import Category, Tag, Cause

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ordering = ['name']

@admin.register(Cause)
class CauseAdmin(admin.ModelAdmin):
    ordering = ['name']
    list_filter = ['category']

admin.site.register(Tag)
