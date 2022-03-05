from django.urls import path

from launio.club.views import show_index, show_contact

urlpatterns = (
    path('', show_index, name='show index'),
    path('contact', show_contact, name='show contact')
)
