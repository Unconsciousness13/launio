from django.urls import path

# urlpatterns = (
#     path('', show_index, name='show index'),
#     path('contact/', show_contact, name='show contact'),
#     path('register/', register_user, name='register page'),
#     path('login/', login_user, name='login page'),
#     path('trainers/', trainers, name='trainers page'),
#     path('directors/', directors, name='directors page'),
#     path('gymnasts/', gymnasts, name='gymnasts page'),
#     path('logout/', UserLogoutView.as_view(), name='logout user'),
# )
from launio.club.views import HomeView, RegisterView

# from launio.club.views import show_index, show_contact, register_user, trainers, directors, gymnasts, login_user, \
#     UserLogoutView

urlpatterns = (
    path('', HomeView.as_view(), name='show index'),
    path('register/', RegisterView.as_view(), name='register page')
)
