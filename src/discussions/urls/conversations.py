from django.urls import include, path

from discussions import views

urlpatterns = [
    path('api/conversations/', include(([
        path('<slug:slug>/replies/', views.reply_collection, name='replies'),
    ], 'conversations-api'))),
]