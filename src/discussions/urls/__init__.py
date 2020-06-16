from django.urls import path, include

urlpatterns = [
    path('', include('discussions.urls.discussions')),
    path('', include('discussions.urls.topics')),
    path('', include('discussions.urls.conversations')),
    path('', include('discussions.urls.replies')),
]