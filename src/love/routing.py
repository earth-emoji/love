from django.urls import path, re_path
from channels.routing import ProtocolTypeRouter, URLRouter, ChannelNameRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator

from notifi.consumers import NotificationConsumer  # Importing notification Consumer from consumers.py
from direct_messages.consumers import MessageConsumer

application = ProtocolTypeRouter({ 
    # Websocket chat handler
    'websocket': AllowedHostsOriginValidator(  # Only allow socket connections from the Allowed hosts in the settings.py file
        AuthMiddlewareStack(  # Session Authentication, required to use if we want to access the user details in the consumer 
            URLRouter(
                [
                    path("notifications/", NotificationConsumer),    # Url path for connecting to the websocket to send notifications.
                    re_path(r'messaging/channel/(?P<pk>[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12})', MessageConsumer),
                ]
            )
        ),
    ),
})