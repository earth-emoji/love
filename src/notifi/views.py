from django.shortcuts import render
from datetime import datetime

# Django Channels
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

def index(request):
    return render(request, "notifications/index.html")

def notify(request):
    # Django Channels Notifications Test
    current_user = request.user
    channel_layer = get_channel_layer()
    data = "notification"+ "...." + str(datetime.now())
    # Trigger message sent to group
    async_to_sync(channel_layer.group_send)(
        str(current_user.pk),  # Channel Name, Should always be string
        {
            "type": "notify",   # Custom Function written in the consumers.py
            "text": data,
        },
    )  
    return render(request, 'notifications/notify.html')