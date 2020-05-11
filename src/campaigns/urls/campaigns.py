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
    ], 'campaigns'))),
    path('volunteers/', include(([
        path('<uuid:slug>/response/', views.volunteer_response, name='volunteer-response'),
    ], 'volunteers'))),
    path('teams/', include(([
        path('create/', views.create_team, name='create'),
        path('<uuid:slug>/', views.team_details, name='details'),
        path('<uuid:team_slug>/leader/<uuid:leader_slug>/', views.make_team_leader, name='leader'),
        path('<uuid:team_slug>/member/<uuid:member_slug>/', views.make_team_member, name='members'),
        path('campaign/<uuid:slug>/', views.team_collection, name='cteams'),
    ], 'teams'))),
]