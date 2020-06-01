from django.urls import path, include

urlpatterns = [
    path('', include('forums.urls.discussions')),
    path('', include('forums.urls.topics')),
    path('', include('forums.urls.posts')),
    path('', include('forums.urls.comments')),
]