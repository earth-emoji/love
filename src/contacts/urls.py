from django.urls import include, path

from contacts import views

urlpatterns = [
    path('contacts/', include(([
        path('', views.contact_list, name='contact-list'),
    ], 'contacts'))),
]