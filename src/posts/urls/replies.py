from django.urls import include, path

from posts import views

urlpatterns = [
    path('api/replies/', include(([
        path('<uuid:slug>/reply/', views.replies_collection, name='reply'),
    ], 'replies-api'))),
]