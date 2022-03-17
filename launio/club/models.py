from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models

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
    pass
    # first_name = FIRST_NAME
    # last_name = LAST_NAME
    # category = MAX_LENGTH_CATEGORY
    # age = AGE
    # photo = models.URLField()
    # description = models.TextField()


class Trainer(models.Model):
    first_name = FIRST_NAME
    last_name = LAST_NAME
    category = MAX_LENGTH_CATEGORY
    age = AGE
    photo = models.URLField()
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
