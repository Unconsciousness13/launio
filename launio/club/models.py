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

AGE = models.IntegerField(
    validators=(
        MinValueValidator(0),
    )
)


class Profile(models.Model):
    USERNAME_MAX_LEN = 15

    AGE_MIN_VALUE = 0

    username = models.CharField(
        max_length=USERNAME_MAX_LEN,
        validators=(
            MinLengthValidator(2),
        )

    )

    email = models.EmailField(

    )

    age = AGE

    profile_image = models.URLField()


class Gymnast(models.Model):
    IMAGE_UPLOAD_TI_DIR = 'gymnasts/'
    first_name = FIRST_NAME
    last_name = LAST_NAME
    category = MAX_LENGTH_CATEGORY
    age = AGE
    photo = models.ImageField(
        upload_to=IMAGE_UPLOAD_TI_DIR,
        null=True,
        blank=True,
        validators=(
            MaxFileSizeInMbValidator(IMAGE_MAX_SIZE_IN_MB),
        )
    )
    description = models.TextField()
    trainer_id = models.ForeignKey('Trainer', on_delete=models.CASCADE)


class Trainer(models.Model):
    IMAGE_UPLOAD_TI_DIR = 'trainers/'
    first_name = FIRST_NAME
    last_name = LAST_NAME
    category = models.CharField(max_length=30)
    age = AGE
    photo = models.ImageField(
        upload_to=IMAGE_UPLOAD_TI_DIR,
        null=True,
        blank=True,
        validators=(
            MaxFileSizeInMbValidator(IMAGE_MAX_SIZE_IN_MB),
        )
    )
    description = models.TextField()


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
