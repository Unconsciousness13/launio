from django.shortcuts import get_object_or_404
from django.views import generic as views
from django.views.generic import TemplateView

from launio.club.forms import AddGymnast, AddTrainer, AddNoteIndividual, AddCompetition, AddNoteTeam, AddTeam
from launio.club.models import Trainer, Gymnast, Team, NotesIndividual, NotesTeam, Competition


class HomeView(views.TemplateView):
    template_name = 'launio/home.html'
    # template_name = 'base/new_test.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['hide_additional_nav_items'] = True
    #     return context
    #
    # def dispatch(self, request, *args, **kwargs):
    #     if request.user.is_autenticated:
    #         return redirect('dashboard')
    #     return super().dispatch(request, *args, **kwargs)


class TrainersView(views.ListView):
    model = Trainer
    template_name = 'launio/trainers.html'
    ordering = 'birthdate', 'train'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class GymnastsView(views.ListView):
    model = Gymnast
    template_name = 'launio/gymnasts.html'
    ordering = 'birthdate', 'first_name'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AddGymnastView(views.FormView):
    template_name = 'launio/add-gymnast.html'
    form_class = AddGymnast
    success_url = '/gymnasts/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class AddTrainerView(views.FormView):
    template_name = 'launio/add-trainer.html'
    form_class = AddTrainer
    success_url = '/trainers/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class DeleteGymnastView(views.DeleteView):
    model = Gymnast
    template_name = 'launio/gymnast-confirm-delete.html'
    success_url = '/gymnasts/'


class DeleteTrainerView(views.DeleteView):
    model = Trainer
    template_name = 'launio/delete-trainer-confirm.html'
    success_url = '/trainers/'


class EditTrainerView(views.UpdateView):
    model = Trainer
    form_class = AddTrainer
    template_name = 'launio/trainer-edit.html'
    success_url = '/trainers/'


class DeleteTeamView(views.DeleteView):
    model = Team
    success_url = '/teams/'


class AddNotesView(views.TemplateView):
    template_name = 'launio/add-notes.html'


class AddNotesIndividualView(views.FormView):
    template_name = 'launio/add-notes-individual.html'
    form_class = AddNoteIndividual
    success_url = '/add-notes/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class AddNotesTeamView(views.FormView):
    template_name = 'launio/add-notes-team.html'
    form_class = AddNoteTeam
    success_url = '/add-notes/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class AddCompetitionView(views.FormView):
    template_name = 'launio/add-competition.html'
    form_class = AddCompetition
    success_url = '/gymnasts/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class AddTeamView(views.FormView):
    template_name = 'launio/add-team.html'
    form_class = AddTeam
    success_url = '/teams/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class TeamsView(views.ListView):
    model = Team
    template_name = 'launio/teams.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class EditGymnastView(views.UpdateView):
    model = Gymnast
    form_class = AddGymnast
    template_name = 'launio/add-gymnast.html'
    success_url = '/gymnasts/'

    # class GymnastDetailView(views.DetailView):


class GymnastDetailView(TemplateView):
    template_name = 'launio/gymnast-details.html'

    def get_context_data(self, **kwargs):
        context = super(GymnastDetailView, self).get_context_data(**kwargs)
        gymnast = get_object_or_404(Gymnast, **kwargs)
        # team = get_object_or_404(Team, **kwargs)
        context['gymnast'] = gymnast
        context['competitions'] = Competition.objects.all()
        context['team'] = Team.objects.filter(gymnast=gymnast.team_id)
        context['notesIndividual'] = NotesIndividual.objects.filter(gymnast=gymnast.id)
        context['notes_team'] = NotesTeam.objects.filter(team=gymnast.team_id)

        return context


class ContactView(views.TemplateView):
    template_name = 'launio/contact.html'
    # form_class = Contact
    # success_url = '/launio/contact-us/'
    #
    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)
