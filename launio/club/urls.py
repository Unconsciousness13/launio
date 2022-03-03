from django.urls import path

from launio.club.views import show_index

urlpatterns = (
    path('', show_index, name='show index'),
)
