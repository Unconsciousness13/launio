from django.urls import path

from launio.club.views import show_index, show_contact, register_user, trainers, directors, gymnasts, login_user

urlpatterns = (
    path('', show_index, name='show index'),
    path('contact/', show_contact, name='show contact'),
    path('register/', register_user, name='register page'),
    path('login/', login_user, name='login page'),
    path('trainers/', trainers, name='trainers page'),
    path('directors/', directors, name='directors page'),
    path('gymnasts/', gymnasts, name='gymnasts page'),

)
