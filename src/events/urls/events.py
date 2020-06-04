from django.urls import include, path

from events import views

urlpatterns = [
    path('events/', include(([
        path('', views.user_events, name='user-events'),
        path('create/', views.create_events, name='create-event'),
    ], 'events'))),
    path('api/events/', include(([
        path('', views.EventListing.as_view(), name='listing')
    ], 'events-api'))),
]