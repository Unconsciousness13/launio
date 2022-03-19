from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models

from validators.image_validator import MaxFileSizeInMbValidator

IMAGE_MAX_SIZE_IN_MB = 5

MAX_FIRST_NAME_LENGTH = 20
MAX_LAST_NAME_LENGTH = 20

MAX_LENGTH_CATEGORY = 20

FIRST_NAME = models.CharField(max_length=MAX_FIRST_NAME_LENGTH, validators=(
    MinValueValidator(2),
))

LAST_NAME = models.CharField(max_length=MAX_LAST_NAME_LENGTH, validators=(
    MinValueValidator(2),
))



class Gymnast(models.Model):
    IMAGE_UPLOAD_TI_DIR = 'gymnasts/'
    first_name = FIRST_NAME
    last_name = LAST_NAME
    category = MAX_LENGTH_CATEGORY
    train = models.CharField(max_length=150)
    birthdate = models.DateField()
    photo = models.ImageField(
        upload_to=IMAGE_UPLOAD_TI_DIR,
        null=True,
        blank=True,
        validators=(
            MaxFileSizeInMbValidator(IMAGE_MAX_SIZE_IN_MB),
        )
    )
    description = models.TextField()

    def train_split(self):
        return self.train.split(' ')


class Trainer(models.Model):
    IMAGE_UPLOAD_TI_DIR = 'trainers/'
    first_name = FIRST_NAME
    last_name = LAST_NAME
    train = models.CharField(max_length=150)
    birthdate = models.DateField()
    photo = models.ImageField(
        upload_to=IMAGE_UPLOAD_TI_DIR,
        null=True,
        blank=True,
        validators=(
            MaxFileSizeInMbValidator(IMAGE_MAX_SIZE_IN_MB),
        )
    )
    description = models.TextField()
    trained_gymnasts_id = models.ForeignKey('Gymnast', on_delete=models.CASCADE)

    def train_split(self):
        return self.train.split(' ')


class Competition(models.Model):
    pass


class NotesIndividual(models.Model):
    pass


class NotesConjunto(models.Model):
    pass


class Team(models.Model):
    pass


class Contact(models.Model):
    first_name = FIRST_NAME
    last_name = LAST_NAME
    email = models.EmailField()
    phone = models.IntegerField()
    message = models.TextField()
