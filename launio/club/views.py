from django.views import generic as views

from launio.club.forms import AddGymnast, AddTrainer, AddNoteIndividual, AddCompetition, AddNoteTeam, AddTeam
from launio.club.models import Trainer, Gymnast, Team


class HomeView(views.TemplateView):
    template_name = 'home.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['hide_additional_nav_items'] = True
    #     return context
    #
    # def dispatch(self, request, *args, **kwargs):
    #     if request.user.is_autenticated:
    #         return redirect('dashboard')
    #     return super().dispatch(request, *args, **kwargs)


class EntrenadorasView(views.ListView):
    model = Trainer
    template_name = 'trainers.html'
    ordering = 'birthdate', 'train'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class GymnastsView(views.ListView):
    model = Gymnast
    template_name = 'gymnasts.html'
    ordering = 'birthdate', 'first_name'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AddGymnastView(views.FormView):
    template_name = 'add-gymnast.html'
    form_class = AddGymnast
    success_url = '/gymnasts/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class AddTrainerView(views.FormView):
    template_name = 'add-trainer.html'
    form_class = AddTrainer
    success_url = '/trainers/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class DeleteGymnastView(views.DeleteView):
    model = Gymnast
    success_url = '/gymnasts/'


class DeleteTrainerView(views.DeleteView):
    model = Trainer
    success_url = '/trainers/'


class DeleteTeamView(views.DeleteView):
    model = Team
    success_url = '/teams/'


class AddNotesView(views.TemplateView):
    template_name = 'add-notes.html'


class AddNotesIndividualView(views.FormView):
    template_name = 'add-notes-individual.html'
    form_class = AddNoteIndividual
    success_url = '/add-notes/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class AddNotesTeamView(views.FormView):
    template_name = 'add-notes-team.html'
    form_class = AddNoteTeam
    success_url = '/add-notes/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class AddCompetitionView(views.FormView):
    template_name = 'add-competition.html'
    form_class = AddCompetition
    success_url = '/gymnasts/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class AddTeamView(views.FormView):
    template_name = 'add-team.html'
    form_class = AddTeam
    success_url = '/teams/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class TeamsView(views.ListView):
    model = Team
    template_name = 'teams.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class EditGymnastView(views.UpdateView):
    model = Gymnast
    fields = 
