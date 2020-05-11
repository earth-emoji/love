from django.urls import include, path

from . import views

urlpatterns = [
    path('logout/', views.logout_view, name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.UserSignUpView.as_view(), name='user_signup'),
    path('members/', include(([
        path('<uuid:slug>/', views.member_index, name='index'),
        path('<uuid:slug>/my-campaigns/', views.initiator_campaign_list, name='ilist'),
        path('<uuid:slug>/campaigns/', views.public_campaign_list, name='plist'),
    ], 'members'))),
]