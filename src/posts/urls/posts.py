from django.urls import include, path

from posts import views

urlpatterns = [
    path('api/posts/', include(([
        path('<uuid:slug>/comment/', views.comment_collection, name='comment'),
        path('campaign/<uuid:slug>/', views.post_collection, name='collection'),
    ], 'posts-api'))),
]