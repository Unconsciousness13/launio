from django.urls import path

from launio.club.views import HomeView, EntrenadorasView, GymnastsView, AddGymnastView, AddTrainerView

urlpatterns = (
    path('', HomeView.as_view(), name='show index'),
    path('trainers/', EntrenadorasView.as_view(), name='show trainers'),
    path('gymnasts/', GymnastsView.as_view, name="show gymnast"),
    path('addgymnast/', AddGymnastView.as_view, name='add gymnast'),
    path('addtrainer/', AddTrainerView.as_view, name='add trainer'),
)
