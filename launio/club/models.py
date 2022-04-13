from cloudinary.models import CloudinaryField
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

# from validators.image_validator import MaxFileSizeInMbValidator

IMAGE_MAX_SIZE_IN_MB = 2
MIN_NAMES_LENGTH_VALIDATOR = 2
MIN_NOTES_VALIDATOR = 0.001
MIN_PLACE_ON_BOARD_VALIDATOR = 1


class Gymnast(models.Model):
    CATEGORIAS = [('Pre-benjamín', 'Pre-benjamín'), ('Benjamín', 'Benjamín'),
                  ('Alevín', 'Alevín'), ('Infantil', 'Infantil'),
                  ('Cadete', 'Cadete')]
    TRAINING_TYPES = [('Individual', 'Individual'), ('Conjunto', 'Conjunto'),
                      ('Individual y Conjunto', 'Individual y Conjunto')]

    first_name = models.CharField(max_length=30, validators=(
        MinLengthValidator(MIN_NAMES_LENGTH_VALIDATOR),))
    last_name = models.CharField(max_length=30, validators=(
        MinLengthValidator(MIN_NAMES_LENGTH_VALIDATOR),))
    category = models.CharField(max_length=30, choices=CATEGORIAS)
    train = models.CharField(max_length=150, choices=TRAINING_TYPES)
    birthdate = models.DateField(blank=True,
                                 null=True)
    photo = CloudinaryField('image'
        # upload_to='gymnasts/',
        # null=True,
        # blank=True,
        # validators=(
        #     MaxFileSizeInMbValidator(IMAGE_MAX_SIZE_IN_MB),
        # )
    )
    description = models.TextField(null=True)
    team = models.ForeignKey('Team', on_delete=models.CASCADE)

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Trainer(models.Model):
    TRAINING_TYPES = [('Individual', 'Individual'), ('Conjunto', 'Conjunto'),
                      ('Individual y Conjunto', 'Individual y Conjunto')]

    first_name = models.CharField(max_length=30, validators=(
        MinLengthValidator(MIN_NAMES_LENGTH_VALIDATOR),))
    last_name = models.CharField(max_length=30, validators=(
        MinLengthValidator(MIN_NAMES_LENGTH_VALIDATOR),))
    train = models.CharField(max_length=150, choices=TRAINING_TYPES)
    birthdate = models.DateField(null=False)
    photo = CloudinaryField(
        'image'
        # upload_to='trainers/',
        # null=True,
        # blank=True,
        # validators=(
        #     MaxFileSizeInMbValidator(IMAGE_MAX_SIZE_IN_MB),
        # )
    )
    description = models.TextField(null=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Competition(models.Model):
    competition_club_organisation = models.CharField(max_length=50, validators=(
        MinLengthValidator(MIN_NAMES_LENGTH_VALIDATOR),))
    competition_name = models.CharField(max_length=50, validators=(
        MinLengthValidator(MIN_NAMES_LENGTH_VALIDATOR),))
    competition_place = models.CharField(max_length=60, null=False)
    competition_date = models.DateField(null=False)

    def __str__(self):
        return self.competition_name


class NotesIndividual(models.Model):
    nota_competition = models.DecimalField(max_digits=5, decimal_places=3,
                                           validators=(MinValueValidator(MIN_NOTES_VALIDATOR),))
    competition = models.ForeignKey('Competition', on_delete=models.CASCADE, )
    gymnast = models.ForeignKey('Gymnast', on_delete=models.CASCADE, )
    competition_place_on_board = models.IntegerField(validators=(MinValueValidator(MIN_PLACE_ON_BOARD_VALIDATOR),))

    def __str__(self):
        return f'{self.gymnast.first_name} {self.gymnast.last_name} {self.competition}'


class NotesTeam(models.Model):
    nota_competition = models.DecimalField(max_digits=5, decimal_places=3,
                                           validators=(MinValueValidator(MIN_NOTES_VALIDATOR),))
    competition = models.ForeignKey('Competition', on_delete=models.CASCADE, )
    team = models.ForeignKey('Team', on_delete=models.CASCADE, )
    competition_place_on_board = models.IntegerField(validators=(MinValueValidator(MIN_PLACE_ON_BOARD_VALIDATOR),))

    def __str__(self):
        return f'{self.team} {self.competition}'


class Team(models.Model):
    name = models.CharField(max_length=30, validators=(
        MinLengthValidator(MIN_NAMES_LENGTH_VALIDATOR),))
    photo = CloudinaryField('image'
        # upload_to='gymnasts/',
        # null=True,
        # blank=True,
        # validators=(
        #     MaxFileSizeInMbValidator(IMAGE_MAX_SIZE_IN_MB),
        # )
    )
    description = models.TextField(null=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    first_name = models.CharField(max_length=30, validators=(
        MinLengthValidator(MIN_NAMES_LENGTH_VALIDATOR),))
    email_address = models.EmailField(null=True)
    message = models.TextField(null=True)
