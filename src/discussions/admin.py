from django.contrib import admin

from discussions.models import Discussion, Topic, Conversation

admin.site.register(Discussion)
admin.site.register(Topic)
admin.site.register(Conversation)
