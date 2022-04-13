from django.test import TestCase, Client
from django.urls import reverse

from launio.club.models import Gymnast, Team


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
