from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.validators import MinLengthValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy

from validators.image_validator import MaxFileSizeInMbValidator

IMAGE_MAX_SIZE_IN_MB = 2
MIN_NAMES_LENGTH_VALIDATOR = 2


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, user_name, first_name, last_name, password, profile_image, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True.')

        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, user_name, first_name, last_name, password, profile_image, **other_fields)

    def create_user(self, email, user_name, first_name, last_name, password, profile_image, **other_fields):
        if not email:
            raise ValueError(gettext_lazy('El email es obligatorio !'))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, first_name=first_name, last_name=last_name,
                          profile_image=profile_image, **other_fields)
        user.set_password(password)
        user.save()


class NewUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(gettext_lazy('email address'), unique=True)
    user_name = models.CharField(max_length=80, unique=True, validators=(
        MinLengthValidator(MIN_NAMES_LENGTH_VALIDATOR),))
    first_name = models.CharField(max_length=80, validators=(
        MinLengthValidator(MIN_NAMES_LENGTH_VALIDATOR),))
    last_name = models.CharField(max_length=80, validators=(
        MinLengthValidator(MIN_NAMES_LENGTH_VALIDATOR),))
    profile_image = models.ImageField(
        upload_to='profile/',
        null=True,
        blank=True,
        validators=(
            MaxFileSizeInMbValidator(IMAGE_MAX_SIZE_IN_MB),
        )
    )
    start_time = models.DateTimeField(default=timezone.now)
    about = models.TextField(gettext_lazy('about'), max_length=400, blank=True, null=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name', 'last_name']

    def __str__(self):
        return self.user_name
