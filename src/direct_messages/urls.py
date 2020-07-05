from django.urls import include, path, re_path

from . import views

UUID_CHANNEL_REGEX = r'channel/(?P<pk>[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12})'

urlpatterns = [
    path('messaging/', include(([
        path("<str:username>/channels", views.user_channels, name="user-channels"),
        re_path(UUID_CHANNEL_REGEX, views.ChannelDetailView.as_view(), name="channel-details"),
        path("<str:username>/", views.PrivateMessageDetailView.as_view(), name="user-messages"),
    ], 'messaging'))),
]