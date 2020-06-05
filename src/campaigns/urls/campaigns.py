from django.urls import include, path

from campaigns import views

urlpatterns = [
    path('campaigns/', include(([
        path('', views.campaign_list, name='list'),
        path('create/', views.campaign_create, name='create'),
        path('<slug:slug>/', views.campaign_details, name='details'),
        path('<slug:slug>/details', views.initiator_campaign_details, name='idetails'),
        path('<slug:slug>/edit/', views.campaign_edit, name='edit'),
        path('<slug:slug>/delete/', views.campaign_delete, name='delete'),
        path('<slug:slug>/volunteer/', views.volunteer_request, name='volunteer-request'),
        path('<slug:slug>/posts/', views.campaign_posts, name='posts'),
    ], 'campaigns'))),
]