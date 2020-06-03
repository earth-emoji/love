from django.urls import include, path

from discussions import views

urlpatterns = [
    path('topics/', include(([
        path('<slug:slug>/', views.topic_thread, name='thread'),
    ], 'topics'))),
    path('api/topics/', include(([
        path('<slug:slug>/entries', views.conversation_collection, name='conversations'),
    ], 'topics-api'))),
]
