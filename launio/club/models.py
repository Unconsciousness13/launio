from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models


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

    age = models.IntegerField(
        validators=(
            MinValueValidator(0),
        )
    )


class Gymnast(models.Model):
    first_name = models.CharField(20)
    last_name = models.CharField(20)
    category = models.CharField(20)
    age = models.IntegerField(validators=MinValueValidator(0))
    photo = models.URLField()
    description = models.TextField()


class Trainers(models.Model):
    first_name = models.CharField(20)
    last_name = models.CharField(20)
    category = models.CharField(20)
    age = models.IntegerField(validators=MinValueValidator(0))
    photo = models.URLField()
    description = models.TextField()


class Competitions(models.Model):
    pass


class Notes(models.Model):
    pass


class Staff(models.Model):
    first_name = models.CharField(20)
    last_name = models.CharField(20)
    category = models.CharField(20)
    age = models.IntegerField(validators=MinValueValidator(0))
    photo = models.URLField()
    description = models.TextField()

