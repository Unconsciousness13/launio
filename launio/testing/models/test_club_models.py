from django.test import TestCase

from launio.club.models import Gymnast, Team, Trainer, Competition, NotesTeam, NotesIndividual


class TestCLubModels(TestCase):

    def test_gymnast__str_(self):
        team = Team.objects.create(name='Benjamin', id=1)
        gymnast = Gymnast.objects.create(first_name='Test', last_name='Testova', category='Benjamin',
                                         birthdate='2000-02-02', team_id=1)
        self.assertEqual(str(gymnast.__str__()), 'Test Testova')

    def test_trainer__str_(self):
        trainer = Trainer.objects.create(first_name='Test', last_name='Testova',
                                         birthdate='2000-02-02')
        self.assertEqual(str(trainer.__str__()), 'Test Testova')

    def test_competition__str_(self):
        competition = Competition.objects.create(competition_club_organisation='Test', competition_name='Red',
                                                 competition_date='2022-02-02', competition_place='Sofia')
        self.assertEqual(str(competition.__str__()), 'Red')

    def test_team_return_on__str_(self):
        team = Team.objects.create(name='RedSox')
        self.assertEqual(str(team.__str__()), 'RedSox')

    def test_notes_team__str_(self):
        competition = Competition.objects.create(competition_club_organisation='Test', competition_name='Red',
                                                 competition_date='2022-02-02', competition_place='Sofia')
        team = Team.objects.create(name='Benjamin', id=1)
        nota = NotesTeam.objects.create(nota_competition=10, competition=competition, team=team,
                                        competition_place_on_board=1)

        self.assertEqual(str(nota.__str__()), 'Benjamin Red')

    def test_notes_individual__str_(self):
        team = Team.objects.create(name='Benjamin', id=1)
        competition = Competition.objects.create(competition_club_organisation='Test', competition_name='Red',
                                                 competition_date='2022-02-02', competition_place='Sofia')
        gymnast = Gymnast.objects.create(first_name='Test', last_name='Testova', category='Benjamin',
                                         birthdate='2000-02-02', team_id=1)

        nota = NotesIndividual.objects.create(nota_competition=10, competition=competition, gymnast=gymnast,
                                              competition_place_on_board=1)

        self.assertEqual(str(nota.__str__()), 'Test Testova Red')
