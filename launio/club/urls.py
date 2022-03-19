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
from launio.club.views import HomeView, EntrenadorasView, GymnastsView, AddGymnastView, AddTrainerView

urlpatterns = (
    path('', HomeView.as_view(), name='show index'),
    path('trainers/', EntrenadorasView.as_view(), name='show trainers'),
    path('gymnasts/', GymnastsView.as_view, name="show gymnast"),
    path('addgymnast/', AddGymnastView.as_view, name='add gymnast'),
    path('addtrainer/', AddTrainerView.as_view, name='add trainer'),
)
