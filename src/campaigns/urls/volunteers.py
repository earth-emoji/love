from django.urls import include, path

from campaigns import views

urlpatterns = [
    path('volunteers/', include(([
        path('<uuid:slug>/response/', views.volunteer_response, name='volunteer-response'),
    ], 'volunteers'))),
]