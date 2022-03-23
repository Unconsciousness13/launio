from django.core.validators import MinLengthValidator
from django.db import models

from validators.image_validator import MaxFileSizeInMbValidator

IMAGE_MAX_SIZE_IN_MB = 2


class Gymnast(models.Model):
    CATEGORIAS = [('prebenjamin', 'Pre-benjamín'), ('prebenjamin', 'Benjamín'),
                  ('prebenjamin', 'Alevín'), ('prebenjamin', 'Infantil'),
                  ('prebenjamin', 'Cadete')]

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
    club_name_competition = models.CharField(max_length=50, null=False)
    place = models.CharField(max_length=60)
    


class NotesIndividual(models.Model):
    pass


class NotesConjunto(models.Model):
    pass


class Team(models.Model):
    categoria = models.CharField(max_length=50)


class Contact(models.Model):
    first_name = models.CharField(max_length=30, validators=(
        MinLengthValidator(2),))
    last_name = models.CharField(max_length=30, validators=(
        MinLengthValidator(2),))
    email = models.EmailField()
    phone = models.IntegerField()
    message = models.TextField()
