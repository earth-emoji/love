from django.urls import include, path

from events import views

urlpatterns = [
    path('events/', include(([
        path('', views.user_events, name='user-events'),
        path('public/', views.public_events, name='public-events'),
        path('create/', views.create_events, name='create-event'),
        path('attend/', views.attend_event, name='attend'),
    ], 'events'))),
    path('api/events/', include(([
        path('', views.EventListing.as_view(), name='listing')
    ], 'events-api'))),
]