from django.urls import path

from launio.club.views import HomeView, TrainersView, GymnastsView, AddGymnastView, AddTrainerView, \
    DeleteGymnastView, AddNotesView, AddNotesIndividualView, AddNotesTeamView, AddCompetitionView, AddTeamView, \
    TeamsView, EditGymnastView, GymnastDetailView, EditTrainerView, DeleteTrainerView, ContactView

urlpatterns = (
    path('', HomeView.as_view(), name='show index'),
    path('trainers/', TrainersView.as_view(), name='show trainers'),
    path('gymnasts/', GymnastsView.as_view(), name="show gymnasts"),
    path('addgymnast/', AddGymnastView.as_view(), name='add gymnast'),
    path('addtrainer/', AddTrainerView.as_view(), name='add trainer'),
    path('delete-gymnast/<int:pk>', DeleteGymnastView.as_view(), name='delete gymnast'),
    path('delete-trainer/<int:pk>', DeleteTrainerView.as_view(), name='delete trainer'),
    path('add-notes/', AddNotesView.as_view(), name='add notes'),
    path('add-notes-individual/', AddNotesIndividualView.as_view(), name='add notes individual'),
    path('add-notes-team/', AddNotesTeamView.as_view(), name='add notes team'),
    path('add-competition/', AddCompetitionView.as_view(), name='add competition'),
    path('add-team/', AddTeamView.as_view(), name='add team'),
    path('teams/', TeamsView.as_view(), name='show teams'),
    path('edit-gymnast/<int:pk>/', EditGymnastView.as_view(), name='edit gymnast'),
    path('edit-trainer/<int:pk>/', EditTrainerView.as_view(), name='edit trainer'),
    path('gymnast-details/<int:pk>/', GymnastDetailView.as_view(), name='detail gymnast'),
    path('contact-us/', ContactView.as_view(), name='contact')

)
