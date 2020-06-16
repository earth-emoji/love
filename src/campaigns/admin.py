from django.contrib import admin

# Register your models here.
from campaigns.models import Campaign, Cause, Volunteer

@admin.register(Cause)
class CauseAdmin(admin.ModelAdmin):
    ordering = ['-name']

admin.site.register(Campaign)
admin.site.register(Volunteer)
