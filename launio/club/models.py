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
