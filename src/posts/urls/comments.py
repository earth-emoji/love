from django.urls import include, path

from posts import views

urlpatterns = [
    path('api/comments/', include(([
        path('<uuid:slug>/reply/', views.reply_collection, name='reply'),
    ], 'comments-api'))),
]