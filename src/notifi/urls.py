from django.urls import include, path

from . import views

urlpatterns = [
    path('notifications/', include(([
        path('', views.index, name='notify-index'),
        path('test/', views.notify, name='test'),
    ], 'notifications'))),
]