from django.core.validators import MinValueValidator
from django.db import models

from validators.image_validator import MaxFileSizeInMbValidator

IMAGE_MAX_SIZE_IN_MB = 1

MAX_FIRST_NAME_LENGTH = 20
MAX_LAST_NAME_LENGTH = 20

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
    category = models.CharField(max_length=50, blank=True,
                                null=True)
    train = models.CharField(max_length=150, blank=True,
                             null=True)
    birthdate = models.DateField(blank=True,
                                 null=True)
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
