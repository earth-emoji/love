from django.urls import include, path

from posts import views

urlpatterns = [
    path('api/posts/', include(([
        path('<slug:slug>/replies/', views.reply_collection, name='replies'),
    ], 'post-api'))),
]