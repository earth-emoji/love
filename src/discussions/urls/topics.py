from django.urls import include, path

from discussions import views

urlpatterns = [
    path('topics/', include(([
        path('<slug:slug>/', views.topic_details, name='details'),
        path('<slug:slug>/new-conversation', views.create_conversation, name='new-conversation'),
    ], 'topics'))),
    path('api/topics/', include(([
        path('<slug:slug>/conversations', views.conversation_collection, name='conversations'),
    ], 'topics-api'))),
]
