from django.test import TestCase, Client
from django.urls import reverse

from launio.club.forms import CreateContactForm, AddNoteIndividual, AddNoteTeam
from launio.club.models import Gymnast, Team, Competition


class ClubGymnastListView(TestCase):

    def test_get__expect_correct_template(self):
        response = self.client.get(reverse('show gymnasts'))

        self.assertTemplateUsed(response, 'launio/gymnasts.html')

    def test_get_when_two_gymnasts_to_contain_to_gymnasts(self):
        team = (Team(id=1, name='Benjamin'),
                Team(id=2, name='Pre-Benjamin'),
                )

        Team.objects.bulk_create(team)

        gymnast_to_create = (
            Gymnast(first_name='Isabella', last_name='Plamenov', category='Benjamin', train='Individual', team_id=1),
            Gymnast(first_name='Plamenov', last_name='Plamenov', category='Benjamin', train='Individual', team_id=2),

        )
        Gymnast.objects.bulk_create(gymnast_to_create)
        response = self.client.get(reverse('show gymnasts'))

        gymnasts = response.context['object_list']

        self.assertEqual(len(gymnasts), 2)

    def test_gymnast_details_page_view(self):
        team = (Team(id=1, name='Benjamin'),
                Team(id=2, name='Pre-Benjamin'),
                )

        Team.objects.bulk_create(team)

        gymnast = Gymnast.objects.create(id=1, first_name='testuser', last_name='lastname', team_id=1)
        client = Client()
        response = client.get("/gymnast-details/1/", follow=True)
        self.assertEqual(response.status_code, 200)

    def test_team_details_page_view(self):
        team = Team.objects.create(id=1, name='Benjamin', description='None', photo='/photo.jpg')
        client = Client()
        response = client.get("/team-details/1/", flolow=True)
        self.assertEqual(response.status_code, 200)

    def test_contact_view_successful(self):
        subject = 'Sended from web La Unio contact form'
        body = {
            'first_name': 'Someone',
            'email_address': 'some@some.com',
            'message': 'Hello',
        }
        message = "\n".join(body.values())
        form = CreateContactForm(body)
        self.assertTrue(form.is_valid())

    def test_add_notes_individual_view__valid_form(self):
        team = Team.objects.create(id=2, name='Benjamin A', description='None', photo='/photo.jpg')
        gymnast = Gymnast.objects.create(id=2, first_name='testuser', last_name='lastname', team_id=2)
        competition = Competition.objects.create(competition_name='BlackroseS', competition_date='2022-03-02',
                                                 competition_club_organisation='Somea')
        context = {
            'nota_competition': 11.100,
            'competition': competition,
            'gymnast': gymnast,
            'competition_place_on_board': 2,

        }
        form = AddNoteIndividual(context)
        self.assertTrue(form.is_valid())

    def test_add_notes_team_view__valid_form(self):
        team = Team.objects.create(id=1, name='Benjamin', description='None', photo='/photo.jpg')
        gymnast = Gymnast.objects.create(id=1, first_name='testuser', last_name='lastname', team_id=1)
        competition = Competition.objects.create(competition_name='Blackrose', competition_date='2022-02-02',
                                                 competition_club_organisation='Some')
        context = {
            'nota_competition': 16.100,
            'competition': competition,
            'team': team,
            'competition_place_on_board': 1,

        }
        form = AddNoteTeam(context)
        self.assertTrue(form.is_valid())
