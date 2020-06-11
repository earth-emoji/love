from django.urls import include, path

from posts import views

urlpatterns = [
    path('posts/', include(([
        path('<slug:slug>/', views.post_details, name='post-details'),
        path('<slug:slug>/details/', views.campaign_post_details, name='campaign-post-details'),
    ], 'posts'))),

    path('api/posts/', include(([
        path('<slug:slug>/comment/', views.comment_collection, name='comment'),
        path('campaign/<slug:slug>/', views.post_collection, name='collection'),
    ], 'posts-api'))),

]
