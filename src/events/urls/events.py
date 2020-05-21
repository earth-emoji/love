from django.urls import include, path

from events import views

urlpatterns = [
    path('api/events/', include(([
        path('', views.EventListing.as_view(), name='listing')
    ], 'events-api'))),
]