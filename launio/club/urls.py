from django.urls import path

from launio.club.views import show_index, show_contact, register_user, login_user

urlpatterns = (
    path('', show_index, name='show index'),
    path('contact', show_contact, name='show contact'),
    path('register', register_user, name='register page'),
    path('login', login_user, name='login page')
)
