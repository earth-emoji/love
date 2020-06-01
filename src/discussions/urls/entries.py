from django.urls import include, path

from discussions import views

urlpatterns = [
    path('api/entry/', include(([
        path('<uuid:slug>/replies/', views.reply_collection, name='replies'),
    ], 'entries-api'))),
]