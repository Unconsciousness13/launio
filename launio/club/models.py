from django.core.validators import MinLengthValidator
from django.db import models

from validators.image_validator import MaxFileSizeInMbValidator

IMAGE_MAX_SIZE_IN_MB = 2


class Gymnast(models.Model):
    CATEGORIAS = [('Pre-benjamín', 'Pre-benjamín'), ('Benjamín', 'Benjamín'),
                  ('Alevín', 'Alevín'), ('Infantil', 'Infantil'),
                  ('Cadete', 'Cadete')]

    first_name = models.CharField(max_length=30, validators=(
        MinLengthValidator(2),))
    last_name = models.CharField(max_length=30, validators=(
        MinLengthValidator(2),))
    category = models.CharField(max_length=30, choices=CATEGORIAS)
    train = models.CharField(max_length=150, blank=True,
                             null=True)
    birthdate = models.DateField(blank=True,
                                 null=True)
    # entrenadora = models.ForeignKey()
    photo = models.ImageField(
        upload_to='gymnasts/',
        null=True,
        blank=True,
        validators=(
            MaxFileSizeInMbValidator(IMAGE_MAX_SIZE_IN_MB),
        )
    )
    description = models.TextField()

    def train_split(self):
        return self.train.split(',')


class Trainer(models.Model):
    first_name = models.CharField(max_length=30, validators=(
        MinLengthValidator(2),))
    last_name = models.CharField(max_length=30, validators=(
        MinLengthValidator(2),))
    train = models.CharField(max_length=150)
    birthdate = models.DateField()
    photo = models.ImageField(
        upload_to='trainers/',
        null=True,
        blank=True,
        validators=(
            MaxFileSizeInMbValidator(IMAGE_MAX_SIZE_IN_MB),
        )
    )
    description = models.TextField()

    def train_split(self):
        return self.train.split(',')


class Competition(models.Model):
    competition_club_organisation = models.CharField(max_length=50, null=False)
    competition_name = models.CharField(max_length=50, null=False)
    competition_place = models.CharField(max_length=60)
    competition_date = models.DateField()


class NotesIndividual(models.Model):
    nota_competition = models.DecimalField(max_digits=5, decimal_places=2)
    competition_id = models.ForeignKey('Competition', on_delete=models.CASCADE, )
    gymnast_id = models.ForeignKey('Gymnast', on_delete=models.CASCADE, )
    competition_place_on_board = models.ImageField(null=False)


class NotesTeam(models.Model):
    nota_competition = models.DecimalField(max_digits=5, decimal_places=2)
    competition_id = models.ForeignKey('Competition', on_delete=models.CASCADE, )
    team_id = models.ForeignKey('Team', on_delete=models.CASCADE, )
    competition_place_on_board = models.ImageField(null=False)


class Team(models.Model):
    category = models.CharField(max_length=50)
    trainers = models.CharField(max_length=150)

    def train_split(self):
        return self.trainers.split(',')


class Contact(models.Model):
    first_name = models.CharField(max_length=30, validators=(
        MinLengthValidator(2),))
    last_name = models.CharField(max_length=30, validators=(
        MinLengthValidator(2),))
    email = models.EmailField()
    phone = models.IntegerField()
    message = models.TextField()
