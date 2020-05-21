from django.urls import include, path

from campaigns import views

urlpatterns = [
    path('campaigns/', include(([
        path('', views.campaign_list, name='list'),
        path('create/', views.campaign_create, name='create'),
        path('<uuid:slug>/', views.campaign_details, name='details'),
        path('<uuid:slug>/details', views.initiator_campaign_details, name='idetails'),
        path('<uuid:slug>/edit/', views.campaign_edit, name='edit'),
        path('<uuid:slug>/delete/', views.campaign_delete, name='delete'),
        path('<uuid:slug>/volunteer/', views.volunteer_request, name='volunteer-request'),
        path('<uuid:slug>/teams/', views.campaign_teams, name='teams'),
        path('<uuid:slug>/posts/', views.campaign_posts, name='posts'),
        path('<uuid:slug>/events/', views.campaign_events, name='events'),
    ], 'campaigns'))),
]