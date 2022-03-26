from django.urls import path

from launio.club.views import HomeView, TrainersView, GymnastsView, AddGymnastView, AddTrainerView, \
    DeleteGymnastView, AddNotesView, AddNotesIndividualView, AddNotesTeamView, AddCompetitionView, AddTeamView, \
    TeamsView, EditGymnastView, GymnastDetailView

urlpatterns = (
    path('', HomeView.as_view(), name='show index'),
    path('trainers/', TrainersView.as_view(), name='show trainers'),
    path('gymnasts/', GymnastsView.as_view(), name="show gymnasts"),
    path('addgymnast/', AddGymnastView.as_view(), name='add gymnast'),
    path('addtrainer/', AddTrainerView.as_view(), name='add trainer'),
    # path('deletegymnast/<int:pk>', DeleteGymnastView.as_view(), 'delete gymnast'),
    path('<pk>/delete/', DeleteGymnastView.as_view()),
    path('add-notes/', AddNotesView.as_view(), name='add notes'),
    path('add-notes-individual/', AddNotesIndividualView.as_view(), name='add notes individual'),
    path('add-notes-team/', AddNotesTeamView.as_view(), name='add notes team'),
    path('add-competition/', AddCompetitionView.as_view(), name='add competition'),
    path('add-team/', AddTeamView.as_view(), name='add team'),
    path('teams/', TeamsView.as_view(), name='show teams'),
    path('edit/<slug:slug>/', EditGymnastView.as_view(), name=' edit gymnast'),
    path('<slug:slug>/', GymnastDetailView.as_view(), name='detail gymnast')

)
