from django.urls import include, path

from campaigns import views

urlpatterns = [
    path('teams/', include(([
        path('create/', views.create_team, name='create'),
        path('<slug:slug>/', views.team_details, name='details'),
        path('<slug:team_slug>/leader/<uuid:leader_slug>/', views.make_team_leader, name='leader'),
        path('<slug:team_slug>/member/<uuid:member_slug>/', views.make_team_member, name='members'),
        path('campaign/<slug:slug>/', views.team_collection, name='cteams'),
    ], 'teams'))),
]