from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.mail import send_mail, BadHeaderError
from django.http import BadHeaderError
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.views import generic as views
from django.views.generic import TemplateView

from launio.club.forms import AddGymnast, AddTrainer, AddNoteIndividual, AddCompetition, AddNoteTeam, AddTeam
from launio.club.models import Trainer, Gymnast, Team, NotesIndividual, NotesTeam, Competition
from .forms import CreateContactForm


class HomeView(views.TemplateView):
    template_name = 'launio/home.html'


class GymnastsView(views.ListView):
    model = Gymnast
    template_name = 'launio/gymnasts.html'
    ordering = 'birthdate', 'first_name'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AddGymnastView(PermissionRequiredMixin, views.FormView):
    permission_required = ('Can add gymnast', 'Can change gymnast')
    template_name = 'launio/add-gymnast.html'
    form_class = AddGymnast
    success_url = '/gymnasts/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class EditGymnastView(PermissionRequiredMixin, views.UpdateView):
    permission_required = ('Can add gymnast', 'Can change gymnast')
    model = Gymnast
    form_class = AddGymnast
    template_name = 'launio/add-gymnast.html'
    success_url = '/gymnasts/'


class DeleteGymnastView(PermissionRequiredMixin, views.DeleteView):
    permission_required = ('Can add gymnast', 'Can change gymnast', 'Can delete gymnast')
    model = Gymnast
    template_name = 'launio/gymnast-confirm-delete.html'
    success_url = '/gymnasts/'


class GymnastDetailView(TemplateView):
    template_name = 'launio/gymnast-details.html'

    def get_context_data(self, **kwargs):
        context = super(GymnastDetailView, self).get_context_data(**kwargs)
        gymnast = get_object_or_404(Gymnast, **kwargs)
        context['gymnast'] = gymnast
        context['competitions'] = Competition.objects.all()
        context['team'] = Team.objects.filter(gymnast=gymnast.team_id)
        context['notesIndividual'] = NotesIndividual.objects.filter(gymnast=gymnast.id)
        context['notes_team'] = NotesTeam.objects.filter(team=gymnast.team_id)

        return context


class AddTrainerView(PermissionRequiredMixin, views.FormView):
    permission_required = ('Can add trainer', 'Can change trainer', 'Can delete trainer')
    template_name = 'launio/add-trainer.html'
    form_class = AddTrainer
    success_url = '/trainers/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class EditTrainerView(PermissionRequiredMixin, views.UpdateView):
    permission_required = ('Can add trainer', 'Can change trainer', 'Can delete trainer')
    model = Trainer
    form_class = AddTrainer
    template_name = 'launio/trainer-edit.html'
    success_url = '/trainers/'


class DeleteTrainerView(PermissionRequiredMixin, views.DeleteView):
    permission_required = ('Can add trainer', 'Can change trainer', 'Can delete trainer')
    model = Trainer
    template_name = 'launio/delete-trainer-confirm.html'
    success_url = '/trainers/'


class TrainersView(views.ListView):
    model = Trainer
    template_name = 'launio/trainers.html'
    ordering = 'birthdate', 'train'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AddTeamView(PermissionRequiredMixin, views.FormView):
    permission_required = ('Can add team', 'Can change team', 'Can delete team')
    template_name = 'launio/add-team.html'
    form_class = AddTeam
    success_url = '/teams/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class EditTeamView(PermissionRequiredMixin, views.UpdateView):
    permission_required = ('Can add team', 'Can change team', 'Can delete team')
    model = Team
    form_class = AddTeam
    template_name = 'launio/team-edit.html'
    success_url = '/teams/'


class DeleteTeamView(PermissionRequiredMixin, views.DeleteView):
    permission_required = ('Can add team', 'Can change team', 'Can delete team')
    model = Team
    template_name = 'launio/team-confirm-delete.html'
    success_url = '/teams/'


class TeamsView(views.ListView):
    model = Team
    template_name = 'launio/teams.html'
    ordering = 'name'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TeamDetailView(TemplateView):
    template_name = 'launio/team-details.html'

    def get_context_data(self, **kwargs):
        context = super(TeamDetailView, self).get_context_data(**kwargs)
        team = get_object_or_404(Team, **kwargs)
        context['team'] = team
        context['gymnast'] = Gymnast.objects.filter(team_id=team.id)
        context['competitions'] = Competition.objects.all()
        context['notes_team'] = NotesTeam.objects.filter(team=team.id)

        return context


class AddNotesView(PermissionRequiredMixin, views.TemplateView):
    permission_required = ('Can add notes', 'Can change notes', 'Can delete notes')
    template_name = 'launio/add-notes.html'


class AddNotesIndividualView(PermissionRequiredMixin, views.FormView):
    permission_required = ('Can add notes individual', 'Can change notes individual', 'Can delete notes individual')
    template_name = 'launio/add-notes-individual.html'
    form_class = AddNoteIndividual
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class AddNotesTeamView(PermissionRequiredMixin, views.FormView):
    permission_required = ('Can add notes team', 'Can change notes team', 'Can delete notes team')
    template_name = 'launio/add-notes-team.html'
    form_class = AddNoteTeam
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class AddCompetitionView(PermissionRequiredMixin, views.FormView):
    permission_required = ('Can add competition', 'Can change competition', 'Can delete competition')
    template_name = 'launio/add-competition.html'
    form_class = AddCompetition
    success_url = '/gymnasts/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def contact_view(request):
    if request.method == 'POST':
        form = CreateContactForm(request.POST)
        if form.is_valid():
            subject = "Sended from web La Unio contact form"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'pakotestpako@gmail.com', ['pakotestpako@gmail.com'])
                messages.success(request, 'Su mensaje ha sido enviado !')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect("contact")

    form = CreateContactForm()

    return render(request, "launio/contact.html", {'form': form})
