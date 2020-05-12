from django.urls import include, path

from campaigns import views

urlpatterns = [
    path('teams/', include(([
        path('create/', views.create_team, name='create'),
        path('<uuid:slug>/', views.team_details, name='details'),
        path('<uuid:team_slug>/leader/<uuid:leader_slug>/', views.make_team_leader, name='leader'),
        path('<uuid:team_slug>/member/<uuid:member_slug>/', views.make_team_member, name='members'),
        path('campaign/<uuid:slug>/', views.team_collection, name='cteams'),
    ], 'teams'))),
]