from django.core.validators import MinLengthValidator
from django.db import models

from validators.image_validator import MaxFileSizeInMbValidator

IMAGE_MAX_SIZE_IN_MB = 2


class Gymnast(models.Model):
    CATEGORIAS = [('Pre-benjamín', 'Pre-benjamín'), ('Benjamín', 'Benjamín'),
                  ('Alevín', 'Alevín'), ('Infantil', 'Infantil'),
                  ('Cadete', 'Cadete')]
    TRAINING_TYPES = [('Individual', 'Individual'), ('Conjunto', 'Conjunto'),
                      ('Individual y Conjunto', 'Individual y Conjunto')]

    slug = models.SlugField(null=True, )
    first_name = models.CharField(max_length=30, validators=(
        MinLengthValidator(2),))
    last_name = models.CharField(max_length=30, validators=(
        MinLengthValidator(2),))
    category = models.CharField(max_length=30, choices=CATEGORIAS)
    train = models.CharField(max_length=150, choices=TRAINING_TYPES)
    birthdate = models.DateField(blank=True,
                                 null=True)
    photo = models.ImageField(
        upload_to='gymnasts/',
        null=True,
        blank=True,
        validators=(
            MaxFileSizeInMbValidator(IMAGE_MAX_SIZE_IN_MB),
        )
    )
    description = models.TextField()
    team = models.ForeignKey('Team', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Trainer(models.Model):
    TRAINING_TYPES = [('Individual', 'Individual'), ('Conjunto', 'Conjunto'),
                      ('Individual y Conjunto', 'Individual y Conjunto')]

    first_name = models.CharField(max_length=30, validators=(
        MinLengthValidator(2),))
    last_name = models.CharField(max_length=30, validators=(
        MinLengthValidator(2),))
    train = models.CharField(max_length=150, choices=TRAINING_TYPES)
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

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Competition(models.Model):
    competition_club_organisation = models.CharField(max_length=50, null=False)
    competition_name = models.CharField(max_length=50, null=False)
    competition_place = models.CharField(max_length=60, null=False)
    competition_date = models.DateField(null=False)

    def __str__(self):
        return self.competition_name


class NotesIndividual(models.Model):
    nota_competition = models.DecimalField(max_digits=5, decimal_places=2, null=False)
    competition = models.ForeignKey('Competition', on_delete=models.CASCADE, )
    gymnast = models.ForeignKey('Gymnast', on_delete=models.CASCADE, )
    competition_place_on_board = models.IntegerField(null=False)


class NotesTeam(models.Model):
    nota_competition = models.DecimalField(max_digits=5, decimal_places=2, null=False)
    competition = models.ForeignKey('Competition', on_delete=models.CASCADE, )
    team = models.ForeignKey('Team', on_delete=models.CASCADE, )
    competition_place_on_board = models.IntegerField(null=False)


class Team(models.Model):
    name = models.CharField(max_length=30, unique=True)
    photo = models.ImageField(
        upload_to='gymnasts/',
        null=True,
        blank=True,
        validators=(
            MaxFileSizeInMbValidator(IMAGE_MAX_SIZE_IN_MB),
        )
    )
    description = models.TextField()

    def __str__(self):
        return self.name

#
# class Contact(models.Model):
#     first_name = models.CharField(max_length=30, validators=(
#         MinLengthValidator(2),))
#     last_name = models.CharField(max_length=30, validators=(
#         MinLengthValidator(2),))
#     email = models.EmailField()
#     phone = models.IntegerField()
#     message = models.TextField()
